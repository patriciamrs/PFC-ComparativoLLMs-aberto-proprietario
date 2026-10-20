
# Análise de Code Smells — Classe Customer

### 1. Data Clumps (Agrupamento de Dados)

**Localização:** Classe `Customer`, método `__init__()` e método `update_contact_info()`.

**Trecho:**

    self.first_name = None
    self.last_name = None
    self.address = None
    self.phone_number = None
    self.email = None

**Justificativa:** Os atributos relacionados às informações pessoais e de contato formam um grupo de dados que aparece conjuntamente na inicialização e no método `update_contact_info()`, caracterizando um agrupamento de dados relacionados.

### 2. Temporary Field (Campo Temporário)

**Localização:** Classe `Customer`, método `__init__()`.

**Trecho:**

    self.temp_discount_code = None
    self.temp_order_note = None

**Justificativa:** Os atributos representam informações temporárias relacionadas a descontos e observações de pedidos. São inicializados com `None` e não são utilizados nos demais métodos apresentados, indicando campos que não participam do comportamento habitual da classe.

### 3. Dead Code (Código Morto)

**Localização:** Métodos `another_unused_method()`, `yet_another_unused_method()` e `refused_bequest()`.

**Trecho:**

    def another_unused_method(self):
        pass

    def yet_another_unused_method(self):
        pass

    def refused_bequest(self):
        pass

**Justificativa:** Os métodos não possuem implementação funcional e não são utilizados em nenhuma parte do código apresentado. Dessa forma, constituem trechos sem comportamento efetivo.

### 4. Message Chains (Cadeias de Mensagens)

**Localização:** Métodos `complain()`, `chain_of_methods()` e `access_internal_details()`.

**Trechos:**

    self.pizza_shop.casher.calm_customer_down()
    self.pizza_shop.casher.chef.clean_kitchen()

    self.pizza_shop.casher.chef.clean_kitchen()

    self.pizza_shop.casher.chef.busy

**Justificativa:** Os métodos acessam objetos por meio de sequências de referências encadeadas, fazendo com que a classe `Customer` dependa da estrutura interna de outros objetos para executar operações ou consultar informações.

### 5. Middle Man (Intermediário)

**Localização:** Método `middle_method()`.

**Trecho:**

    def middle_method(self):
        print("Middleman method delegating to another method")
        self.real_method()

**Justificativa:** O método atua principalmente como intermediário, encaminhando a execução para `real_method()` sem acrescentar lógica significativa à operação, além da mensagem exibida.

### 6. Long Parameter List (Lista Longa de Parâmetros — Não Confirmado)

**Localização:** Método `order_with_unnecessary_details()`.

**Trecho:**

    self.order_pizza(
        "Veggie", "Large", "Whole Wheat", "Veggies",
        False, True, False, False, "Olives", "Mushrooms",
        "Pesto", "Thick", False, False, True, True,
        True, False, False, False
    )

**Justificativa:** A chamada apresenta uma quantidade excessiva de argumentos, dificultando a compreensão de seus significados. Entretanto, o método `order_pizza()` recebe apenas um argumento além de `self`, tornando a chamada incompatível com sua assinatura. Portanto, não é possível confirmar esse code smell na declaração do método.

### 7. Duplicated Code (Código Duplicado)

**Localização:** Método `duplicate_complaint()`.

**Trecho:**

    self.complain("Pizza is cold")
    self.complain("Pizza is cold")
    self.complain("Pizza is late")
    self.complain("Pizza is late")

**Justificativa:** Existem chamadas idênticas repetidas consecutivamente, executando as mesmas operações com os mesmos argumentos, caracterizando duplicação de código.

### 8. Divergent Change (Mudança Divergente — Indício)

**Localização:** Classe `Customer`, especialmente os métodos relacionados a pedidos, reclamações, informações de contato e promoções.

**Trechos:**

    def order_pizza(self, pizza_type: str):

    def handle_complaint(self, complaint):

    def update_contact_info(self, first_name, last_name, address, phone_number, email):

    def notify_for_promotion(self):

    def apply_loyalty_points(self):

**Justificativa:** A classe concentra responsabilidades relacionadas a pedidos, reclamações, informações pessoais, notificações e benefícios comerciais. Essas funcionalidades representam diferentes motivos para alterações na mesma classe, indicando um possível caso de mudança divergente.

### 9. Primitive Obsession (Obsessão por Primitivos)

**Localização:** Método `handle_complaint()`.

**Trecho:**

    if complaint == "cold pizza":
        self.complain("Pizza is cold")
    elif complaint == "late delivery":
        self.complain("Pizza is late")
    elif complaint == "wrong order":
        self.complain("Wrong pizza delivered")

**Justificativa:** O método utiliza valores textuais específicos para representar categorias de reclamação e controlar o comportamento do programa. Essa representação de conceitos do domínio por strings caracteriza o uso de tipos primitivos para representar diferentes situações.

---

## Resumo dos Code Smells

| Code Smell | Localização |
|---|---|
| Data Clumps | `__init__()`, `update_contact_info()` |
| Temporary Field | `temp_discount_code`, `temp_order_note` |
| Dead Code | `another_unused_method()`, `yet_another_unused_method()`, `refused_bequest()` |
| Message Chains | `complain()`, `chain_of_methods()`, `access_internal_details()` |
| Middle Man | `middle_method()` |
| Long Parameter List | `order_with_unnecessary_details()` — não confirmado |
| Duplicated Code | `duplicate_complaint()` |
| Divergent Change | Classe `Customer` — indício |
| Primitive Obsession | `handle_complaint()` |

**Observações:** O método `long_complaint_method()` não é suficientemente extenso ou complexo para confirmar Long Function apenas pelo nome ou pela quantidade de chamadas. Da mesma forma, `refused_bequest()` não comprova Refused Bequest, pois não há herança apresentada. Long Parameter List e Divergent Change não foram confirmados de forma conclusiva e devem ser tratados separadamente dos code smells identificados.
