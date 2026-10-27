
# Análise de Code Smells — Classe `Chef` (Python)

## 1. Large Class (Classe Grande)

- **Localização:** Classe `Chef`.
- **Justificativa:** A classe possui muitos atributos e métodos com responsabilidades diferentes, incluindo preparação de pizzas, gerenciamento de informações de clientes, aplicação de descontos, notificações promocionais e tratamento de reclamações. Essa concentração de funcionalidades indica que a classe assume responsabilidades excessivas.

## 2. Long Method (Método Longo)

- **Localização:** Método `long_method()`.
- **Justificativa:** O método reúne diversas operações de naturezas diferentes, como preparar pizzas, limpar a cozinha, atualizar informações de contato, enviar notificações e aplicar descontos. A quantidade e a diversidade de tarefas realizadas tornam o método complexo e dificultam sua compreensão.

## 3. Long Parameter List (Lista Longa de Parâmetros)

- **Localização:** Métodos `order_with_unnecessary_details()` e `update_contact_info()`.
- **Justificativa:** O método `order_with_unnecessary_details()` recebe seis parâmetros relacionados a características e condições de um pedido. Já `update_contact_info()` recebe cinco parâmetros referentes a informações pessoais. Essas listas extensas aumentam a quantidade de informações necessárias para realizar as chamadas.

## 4. Data Clumps (Agrupamentos de Dados)

- **Localização:** Atributos `first_name`, `last_name`, `address`, `phone_number` e `email`, além do método `update_contact_info()`.
- **Justificativa:** Os atributos representam um conjunto de informações relacionadas ao contato de um cliente e aparecem agrupados tanto na declaração dos atributos quanto nos parâmetros do método. Essa repetição sugere a existência de um grupo de dados com significado próprio.

## 5. Primitive Obsession (Obsessão por Tipos Primitivos)

- **Localização:** Atributos `frequent_customer_discount`, `first_name`, `last_name`, `address`, `phone_number`, `email` e `temp_discount_code`, além dos parâmetros de `order_with_unnecessary_details()`.
- **Justificativa:** O código utiliza valores primitivos para representar conceitos como informações de contato, descontos e características de pedidos, sem estruturas específicas que representem esses conceitos e suas regras.

## 6. Divergent Change (Mudança Divergente)

- **Localização:** Classe `Chef`.
- **Justificativa:** A classe concentra funcionalidades relacionadas a diferentes áreas do sistema. Alterações no preparo de pizzas, nas informações dos clientes, nas promoções ou no atendimento de reclamações podem exigir modificações na mesma classe, indicando múltiplos motivos para mudanças.

## 7. Feature Envy (Inveja de Funcionalidade)

- **Localização:** Método `cut_pizza_and_put_in_box()`.
- **Trecho:**

```python
print(f"Chef is cutting the {self.pizza.topping} pizza and putting it in a box.")
```

- **Justificativa:** O método acessa diretamente o atributo `topping` de um objeto `Pizza`. Entretanto, esse acesso isolado não é suficiente para caracterizar com segurança o *Feature Envy*, pois o método não demonstra dependência predominante dos dados ou comportamentos de outra classe.

## 8. Duplicate Code (Código Duplicado)

- **Localização:** Métodos `handle_complaint()` e `duplicate_method()`.
- **Trechos:**

```python
if complaint == "cold pizza":
    self.clean_kitchen()
elif complaint == "late delivery":
    self.clean_kitchen()
elif complaint == "wrong order":
    self.clean_kitchen()
else:
    self.clean_kitchen()
```

```python
self.bake_pizza("Cheese")
self.bake_pizza("Cheese")
```

- **Justificativa:** Em `handle_complaint()`, todos os caminhos condicionais executam exatamente a mesma operação, independentemente da reclamação. Em `duplicate_method()`, a mesma chamada é executada duas vezes consecutivas, embora essa repetição possa ser intencional.

## 9. Dead Code (Código Morto)

- **Localização:** Métodos `another_unused_method()`, `yet_another_unused_method()` e `refused_bequest()`.
- **Trecho:**

```python
def another_unused_method(self):
    pass

def yet_another_unused_method(self):
    pass

def refused_bequest(self):
    pass
```

- **Justificativa:** Os métodos possuem apenas a instrução `pass`, sem implementar qualquer comportamento. Não apresentam funcionalidade útil no código fornecido. Sua ausência de uso no restante do projeto, porém, não pode ser confirmada apenas por esta classe.

## 10. Speculative Generality (Generalidade Especulativa)

- **Localização:** Métodos `another_unused_method()`, `yet_another_unused_method()` e `refused_bequest()`.
- **Justificativa:** Os métodos apresentam declarações sem implementação e sem uma finalidade funcional identificável no trecho analisado. Podem representar funcionalidades antecipadas sem necessidade atual, embora não seja possível confirmar essa intenção apenas pelo código.

## 11. Middle Man (Intermediário)

- **Localização:** Métodos `middleman_method()` e `middle_method()`.
- **Trecho:**

```python
def middleman_method(self):
    print("Chef is calling a middleman method")
    self.middle_method()

def middle_method(self):
    print("Middleman method delegating to another method")
    self.real_method()
```

- **Justificativa:** Os métodos criam níveis intermediários de chamadas até alcançar `real_method()`, sem acrescentar uma operação relevante além de mensagens informativas. Isso introduz uma cadeia de delegações desnecessária.

## 12. Lazy Element (Elemento Preguiçoso)

- **Localização:** Métodos `middleman_method()`, `middle_method()` e `chain_of_methods()`.
- **Justificativa:** Esses métodos possuem pouca lógica própria e basicamente encaminham a execução para outros métodos, acrescentando apenas mensagens simples. Sua existência proporciona pouca funcionalidade em relação à estrutura adicional introduzida.

## 13. Temporary Field (Campo Temporário)

- **Localização:** Atributos `temp_discount_code` e `temp_order_note`, definidos em `__init__()`.
- **Justificativa:** Os atributos são declarados, mas não são utilizados nos demais métodos apresentados. Seus nomes sugerem informações destinadas a situações específicas, e não ao estado permanente da classe. Entretanto, não há uso suficiente para confirmar que esses campos são efetivamente temporários.

## 14. Switch Statements / Repeated Switches (Condicionais Repetitivas)

- **Localização:** Método `handle_complaint()`.
- **Justificativa:** O método apresenta uma sequência de condições que verificam diferentes tipos de reclamação. Entretanto, todas as alternativas executam a mesma ação. Trata-se de lógica condicional redundante, não sendo possível confirmar o smell *Repeated Switches* de Fowler, que envolve a repetição de estruturas de decisão semelhantes em diferentes partes do sistema.

---

## Considerações sobre a identificação

Os indícios mais claros no código são **Large Class, Long Method, Long Parameter List, Data Clumps, Divergent Change, Duplicate Code e Middle Man**.

Os demais casos apresentados possuem ressalvas: alguns são indícios possíveis, mas não podem ser confirmados como *code smells* apenas com o trecho disponível. Em particular, `Refused Bequest` não está demonstrado, pois a classe `Chef` não apresenta herança, e a existência de métodos vazios não comprova, por si só, código morto.

Também há uma inconsistência funcional em `order_with_unnecessary_details()`: a chamada `self.apply_discount(discount_code)` fornece um argumento a um método declarado sem parâmetros adicionais. Isso pode provocar um `TypeError`, mas corresponde a um defeito de implementação, não necessariamente a um *code smell*.
