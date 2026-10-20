# Análise de Code Smells — Código Python

## 1. Large Class (Classe Grande)

**Localização:** Classe `Pizza`.

**Justificativa:** A classe `Pizza` concentra diversas responsabilidades, incluindo configuração da pizza, gerenciamento de informações do cliente, notificações promocionais, aplicação de descontos, tratamento de reclamações e processamento de pedidos. Essa concentração de funcionalidades distintas caracteriza uma classe com responsabilidades excessivas.

## 2. Data Clumps (Agrupamentos de Dados)

**Localização:** Atributos da classe `Pizza` e método `update_customer_info()`.

**Trecho:**
    self.customer_first_name = None
    self.customer_last_name = None
    self.customer_address = None
    self.customer_phone_number = None
    self.customer_email = None

**Justificativa:** Os atributos relacionados às informações pessoais do cliente formam um conjunto de dados logicamente associado. Esse mesmo agrupamento aparece nos parâmetros do método `update_customer_info()`, indicando a presença de dados que são tratados em conjunto.

## 3. Temporary Field (Campo Temporário)

**Localização:** Construtor `__init__()` da classe `Pizza`.

**Trecho:**
    self.temp_discount_code = None
    self.temp_order_note = None

**Justificativa:** Os atributos `temp_discount_code` e `temp_order_note` são declarados sem valores iniciais significativos e não são utilizados pelos métodos apresentados. Seus nomes indicam uma finalidade temporária, embora o código não demonstre efetivamente seu uso condicionado a situações específicas. Portanto, trata-se de um indício, não de uma ocorrência confirmada.

## 4. Long Method (Método Longo)

**Localização:** Método `long_method()` da classe `Pizza`.

**Trecho:**
    def long_method(self):
        print("Pizza is handling many tasks in a single method")
        self.set_size("Large")
        self.set_dough_type("Thin Crust")
        self.set_topping("Pepperoni")
        self.update_customer_info("John", "Doe", "123 Street", "555-5555", "john.doe@example.com")
        self.notify_for_promotion()
        self.notify_for_discount()
        self.notify_for_new_arrivals()
        self.apply_discount()
        self.apply_loyalty_points()
        self.handle_complaint("cold pizza")

**Justificativa:** O método reúne diversas operações de naturezas diferentes, como atualização de características da pizza, gerenciamento de informações do cliente, notificações, descontos e reclamações. Apesar de não possuir muitas linhas, apresenta uma concentração de responsabilidades que caracteriza o code smell.

## 5. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Métodos `update_customer_info()` e `order_with_unnecessary_details()` da classe `Pizza`.

**Trechos:**
    def update_customer_info(self, first_name, last_name, address, phone_number, email):

    def order_with_unnecessary_details(self, pizza_type, size, crust_type, toppings, extra_cheese, discount_code):

**Justificativa:** Os métodos recebem, respectivamente, cinco e seis parâmetros explícitos, aumentando a quantidade de informações necessárias para realizar suas chamadas. Essa característica torna as interfaces mais complexas e pode dificultar a compreensão e manutenção do código.

## 6. Duplicate Code (Código Duplicado)

**Localização:** Método `duplicate_method()` da classe `Pizza`.

**Trecho:**
    def duplicate_method(self):
        print("Customer is making a duplicate order")
        self.set_topping("Cheese")
        self.set_topping("Cheese")

**Justificativa:** A chamada `self.set_topping("Cheese")` é repetida consecutivamente com os mesmos argumentos, sem operações intermediárias que justifiquem a repetição. Isso representa duplicação literal de código.

## 7. Repeated Switches (Estruturas Condicionais Repetidas)

**Localização:** Método `handle_complaint()` da classe `Pizza`.

**Trecho:**
    def handle_complaint(self, complaint):
        if complaint == "cold pizza":
            print("Handling complaint: Pizza is cold")
        elif complaint == "late delivery":
            print("Handling complaint: Pizza is late")
        elif complaint == "wrong order":
            print("Handling complaint: Wrong pizza delivered")
        else:
            print("Handling complaint: General complaint")

**Justificativa:** O método utiliza uma sequência de condições para selecionar comportamentos de acordo com o tipo de reclamação. Entretanto, essa estrutura aparece apenas uma vez no código apresentado. Portanto, não há evidência suficiente para caracterizar o code smell `Repeated Switches`.

## 8. Middle Man (Intermediário)

**Localização:** Métodos `middleman_method()` e `middle_method()` da classe `Pizza`.

**Trecho:**
    def middleman_method(self):
        print("Pizza is calling a middleman method")
        self.middle_method()

    def middle_method(self):
        print("Middleman method delegating to another method")
        self.real_method()

**Justificativa:** Os métodos realizam mensagens de saída e encaminham a execução para outros métodos, sem acrescentar processamento significativo. Essa cadeia de delegações apresenta comportamento de intermediação, embora não demonstre que a classe inteira atue predominantemente como intermediária.

## 9. Lazy Class (Classe Preguiçosa)

**Localização:** Classes `VeggiePizza`, `TunaPizza` e `PepperoniPizza`.

**Trechos:**
    class VeggiePizza(Pizza):
        def __init__(self):
            super().__init__("Medium", "Whole Wheat", "Veggies")

    class TunaPizza(Pizza):
        def __init__(self):
            super().__init__("Large", "Thin Crust", "Tuna")

    class PepperoniPizza(Pizza):
        def __init__(self):
            super().__init__("Large", "Regular", "Pepperoni")

**Justificativa:** As três subclasses apenas inicializam a classe `Pizza` com valores específicos, sem apresentar comportamentos adicionais. Essa implementação reduzida pode indicar classes cuja existência oferece pouca funcionalidade própria, caracterizando possíveis ocorrências de `Lazy Class`.

## 10. Speculative Generality (Generalidade Especulativa)

**Localização:** Métodos `another_unused_method()`, `yet_another_unused_method()` e `refused_bequest()` da classe `Pizza`.

**Trecho:**
    def another_unused_method(self):
        pass

    def yet_another_unused_method(self):
        pass

    def refused_bequest(self):
        pass

**Justificativa:** Os três métodos são declarados sem implementação e não são utilizados no código apresentado. Isso sugere a existência de estruturas sem finalidade funcional demonstrada, possivelmente adicionadas para necessidades futuras que ainda não foram concretizadas.

---

## Resumo da Análise

| Code Smell | Localização | Avaliação |
|---|---|---|
| Large Class | Classe `Pizza` | Identificado |
| Data Clumps | Atributos do cliente e `update_customer_info()` | Identificado |
| Temporary Field | `temp_discount_code`, `temp_order_note` | Indício, não confirmado |
| Long Method | `long_method()` | Identificado |
| Long Parameter List | `update_customer_info()`, `order_with_unnecessary_details()` | Identificado |
| Duplicate Code | `duplicate_method()` | Identificado |
| Repeated Switches | `handle_complaint()` | Não confirmado |
| Middle Man | `middleman_method()`, `middle_method()` | Indício de delegação |
| Lazy Class | `VeggiePizza`, `TunaPizza`, `PepperoniPizza` | Possível ocorrência |
| Speculative Generality | Três métodos vazios | Possível ocorrência |

**Observação:** Os métodos vazios não comprovam, por si só, `Speculative Generality`; atributos não utilizados também não comprovam `Temporary Field`. Da mesma forma, o nome `refused_bequest()` não caracteriza `Refused Bequest`, pois não há evidência de rejeição de comportamento herdado. A chamada `chain_of_methods()` também não configura `Message Chains`, pois apresenta apenas uma chamada direta.