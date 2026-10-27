# Análise de Code Smells — Classe Customer (Python)

### 1. Large Class (Classe Grande)

**Localização:** Classe `Customer`.

**Justificativa:** A classe possui muitos atributos e métodos, concentrando responsabilidades relacionadas a pedidos, reclamações, dados pessoais, descontos, notificações e bebidas. Essa diversidade de responsabilidades caracteriza uma classe com funcionalidades excessivas.

### 2. Duplicate Code (Código Duplicado)

**Localização:** Método `duplicate_complaint()`.

**Trecho:**
    self.complain("Pizza is cold")
    self.complain("Pizza is cold")
    self.complain("Pizza is late")
    self.complain("Pizza is late")

**Justificativa:** As mesmas chamadas são repetidas consecutivamente, representando duplicação de instruções sem diferença de comportamento entre as ocorrências.

### 3. Message Chains (Cadeias de Mensagens)

**Localização:** Métodos `complain()`, `chain_of_methods()` e `access_internal_details()`.

**Trechos:**
    self.pizza_shop.casher.chef.clean_kitchen()
    self.pizza_shop.casher.chef.busy

**Justificativa:** Os métodos acessam objetos por meio de uma sequência de referências, atravessando diferentes níveis da estrutura interna de outras classes. Isso aumenta o acoplamento e cria dependência da organização interna dos objetos.

### 4. Middle Man (Intermediário)

**Localização:** Métodos `middleman_method()` e `middle_method()`.

**Trecho:**
    def middleman_method(self):
        print("Customer is calling a middleman method")
        self.middle_method()

    def middle_method(self):
        print("Middleman method delegating to another method")
        self.real_method()

**Justificativa:** Os métodos funcionam principalmente como intermediários, encaminhando a execução até `real_method()`, sem acrescentar lógica significativa além das mensagens exibidas.

### 5. Feature Envy (Inveja de Funcionalidade)

**Localização:** Métodos `complain()` e `access_internal_details()`.

**Trechos:**
    self.pizza_shop.casher.calm_customer_down()
    self.pizza_shop.casher.chef.clean_kitchen()
    self.pizza_shop.casher.chef.busy

**Justificativa:** Esses métodos dependem de funcionalidades e informações pertencentes a outros objetos, especialmente `Cashier` e `Chef`, indicando que parte de seu comportamento está fortemente relacionada a responsabilidades externas à classe `Customer`.

---

## Possíveis Code Smells que exigem análise adicional

### 6. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Método `order_with_unnecessary_details()`.

**Justificativa:** A chamada de `order_pizza()` contém 20 argumentos, dificultando sua compreensão. Entretanto, a assinatura do método aceita apenas um argumento além de `self`, caracterizando também um erro de chamada. Não é possível confirmar o code smell Long Parameter List apenas por essa ocorrência.

### 7. Data Clumps (Agrupamentos de Dados)

**Localização:** Método `update_contact_info()` e atributos de identificação e contato.

**Justificativa:** Os dados de identificação e contato, como nome, sobrenome, endereço, telefone e e-mail, são tratados em conjunto. Isso sugere um agrupamento de informações relacionadas, mas não é suficiente para confirmar o code smell sem identificar agrupamentos recorrentes.

### 8. Speculative Generality (Generalidade Especulativa)

**Localização:** Métodos `another_unused_method()`, `yet_another_unused_method()` e `refused_bequest()`.

**Justificativa:** Esses métodos são declarados sem qualquer implementação ou comportamento efetivo. Sua presença sugere funcionalidades desnecessárias ou previstas para o futuro, mas não é possível confirmar essa intenção apenas pelo código apresentado.

### 9. Long Method (Método Longo)

**Localização:** Método `long_complaint_method()`.

**Justificativa:** O método concentra diversas chamadas relacionadas a reclamações. Entretanto, apresenta poucas linhas e baixa complexidade, tornando discutível sua classificação como Long Method.

---

## Observação

O code smell **Refused Bequest** não foi identificado, pois a classe `Customer` não apresenta herança. A existência de um método chamado `refused_bequest()` não é suficiente para caracterizá-lo.

Os code smells com evidências mais claras são **Large Class, Duplicate Code, Message Chains, Middle Man e Feature Envy**.
