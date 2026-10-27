
# Análise dos Code Smells — Classe Cashier (Python)

## 1. Large Class (Classe Grande)

**Localização:** Classe `Cashier`.

**Justificativa:** A classe concentra diversas responsabilidades, incluindo gerenciamento de pedidos, comunicação com o chef, informações de clientes, notificações promocionais, descontos e tratamento de reclamações. Essa variedade de responsabilidades indica uma classe que acumula funcionalidades de diferentes áreas do sistema.

## 2. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Métodos `order_with_unnecessary_details()` e `update_contact_info()`.

**Trechos:**

`def order_with_unnecessary_details(self, pizza_type, size, crust_type, toppings, extra_cheese, discount_code):`

`def update_contact_info(self, first_name, last_name, address, phone_number, email):`

**Justificativa:** Os métodos recebem uma quantidade elevada de parâmetros, dificultando a compreensão das chamadas e aumentando a complexidade do gerenciamento dos dados necessários para executar suas operações.

## 3. Data Clumps (Agrupamentos de Dados)

**Localização:** Atributos `first_name`, `last_name`, `address`, `phone_number` e `email`, presentes no construtor e utilizados em `update_contact_info()`.

**Trecho:**

    self.first_name = None
    self.last_name = None
    self.address = None
    self.phone_number = None
    self.email = None

**Justificativa:** Os atributos representam um conjunto de informações relacionadas ao contato do cliente, que aparecem agrupadas tanto na definição dos atributos quanto nos parâmetros do método de atualização.

## 4. Dead Code (Código Morto)

**Localização:** Métodos `another_unused_method()`, `yet_another_unused_method()` e `refused_bequest()`.

**Trecho:**

    def another_unused_method(self):
        pass

    def yet_another_unused_method(self):
        pass

    def refused_bequest(self):
        pass

**Justificativa:** Os métodos possuem corpos vazios, contendo apenas a instrução `pass`, e não apresentam qualquer comportamento funcional. Sua presença não contribui para as operações implementadas na classe.

## 5. Duplicate Code (Código Duplicado)

**Localização:** Método `duplicate_method()`.

**Trecho:**

    def duplicate_method(self):
        print("Customer is making a duplicate order")
        self.take_order("Cheese")
        self.take_order("Cheese")

**Justificativa:** A mesma chamada de método, com os mesmos argumentos, é executada consecutivamente, caracterizando repetição de instruções dentro do mesmo método.

## 6. Middle Man (Intermediário)

**Localização:** Métodos `middleman_method()` e `middle_method()`.

**Trecho:**

    def middleman_method(self):
        print("Cashier is calling a middleman method")
        self.middle_method()

    def middle_method(self):
        print("Middleman method delegating to another method")
        self.real_method()

**Justificativa:** Os métodos atuam principalmente como intermediários na execução de outras operações, encaminhando chamadas sucessivas até `real_method()`, sem acrescentar processamento significativo além das mensagens exibidas.

## 7. Inappropriate Intimacy (Intimidade Inapropriada)

**Localização:** Método `access_internal_details()`.

**Trecho:**

    def access_internal_details(self):
        print(f"Accessing internal details: {self.chef.busy}")

**Justificativa:** A classe `Cashier` acessa diretamente o atributo `busy` de um objeto `Chef`, demonstrando conhecimento sobre o estado interno de outra classe e criando dependência de detalhes de sua implementação.

## 8. Divergent Change (Mudança Divergente)

**Localização:** Classe `Cashier`, especialmente os métodos de atualização de informações, notificações, gerenciamento de pedidos e descontos.

**Justificativa:** A classe reúne funcionalidades de diferentes responsabilidades. Assim, alterações nas regras de pedidos, nos dados dos clientes, nas notificações ou nos descontos podem exigir modificações na mesma classe por motivos distintos.

## 9. Speculative Generality (Generalidade Especulativa)

**Localização:** Atributos `temp_discount_code` e `temp_order_note`, além dos métodos vazios da classe.

**Trecho:**

    self.temp_discount_code = None
    self.temp_order_note = None

**Justificativa:** Os atributos são declarados, mas não apresentam utilização no código fornecido. Juntamente com os métodos sem implementação, sugerem estruturas adicionadas para funcionalidades que não estão efetivamente desenvolvidas ou utilizadas.

## 10. Repeated Switches (Condicionais Repetitivas)

**Localização:** Método `handle_complaint()`.

**Trecho:**

    def handle_complaint(self, complaint):
        if complaint == "cold pizza":
            self.calm_customer_down()
        elif complaint == "late delivery":
            self.calm_customer_down()
        elif complaint == "wrong order":
            self.calm_customer_down()
        else:
            self.calm_customer_down()

**Justificativa:** O método apresenta uma estrutura condicional com diferentes casos de reclamação, mas todos executam exatamente a mesma operação. Isso torna as verificações redundantes. Embora haja redundância condicional, não é possível confirmar o smell específico *Repeated Switches*, pois não existem estruturas condicionais equivalentes repetidas em outros pontos do código.

---

## Observações sobre outros possíveis Code Smells

Alguns trechos podem sugerir outros *code smells*, mas não apresentam evidências suficientes para uma identificação conclusiva:

- **Long Method:** Apesar do nome `long_method()`, o método possui poucas instruções e não apresenta extensão ou complexidade suficientes para confirmar esse smell.

- **Message Chains:** O método `chain_of_methods()` realiza apenas `self.chef.clean_kitchen()`, não constituindo uma cadeia de chamadas.

- **Refused Bequest:** O método `refused_bequest()` está vazio, mas não há relação de herança demonstrando rejeição de funcionalidades herdadas.

- **Feature Envy:** A utilização de métodos de `Chef` pela classe `Cashier` não demonstra, isoladamente, que um método esteja excessivamente interessado nos dados de outra classe.

**Nota sobre a classificação:** Os casos de *Dead Code*, *Duplicate Code* e *Middle Man* também exigem cautela. Métodos vazios são observáveis, mas a ausência de chamadas externas não pode ser comprovada apenas por esta classe; chamadas duplicadas podem ser intencionais; e os métodos intermediários contêm mensagens próprias. Portanto, são indícios de smells cuja confirmação depende parcialmente do contexto do sistema.
