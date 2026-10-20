# Análise de Code Smells — Classe `Cashier`

## 1. Data Clumps (Agrupamento de Dados)

**Localização:** Classe `Cashier`, métodos `__init__()` e `update_contact_info()`.

**Trecho:**
```python
self.first_name = None
self.last_name = None
self.address = None
self.phone_number = None
self.email = None
```

**Justificativa:** Os atributos relacionados às informações pessoais e de contato aparecem agrupados na classe e são utilizados em conjunto no método `update_contact_info()`. Esses dados representam um grupo de informações relacionadas, caracterizando o *Data Clumps*.

## 2. Temporary Field (Campo Temporário)

**Localização:** Classe `Cashier`, método `__init__()`.

**Trecho:**
```python
self.temp_discount_code = None
self.temp_order_note = None
```

**Justificativa:** Os atributos são inicializados com `None` e não são utilizados pelos demais métodos da classe. São campos aparentemente destinados a situações específicas, permanecendo sem utilização no código apresentado.

## 3. Dead Code (Código Morto)

**Localização:** Métodos `another_unused_method()`, `yet_another_unused_method()` e `refused_bequest()`.

**Trecho:**
```python
def another_unused_method(self):
    pass

def yet_another_unused_method(self):
    pass

def refused_bequest(self):
    pass
```

**Justificativa:** Os três métodos não possuem implementação e não são chamados em nenhum ponto do código apresentado. Não desempenham qualquer funcionalidade observável na classe.

## 4. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Método `order_with_unnecessary_details()`.

**Trecho:**
```python
def order_with_unnecessary_details(self, pizza_type, size, crust_type, toppings, extra_cheese, discount_code):
```

**Justificativa:** O método recebe seis parâmetros, aumentando a quantidade de informações necessárias para sua chamada. Além disso, parte desses parâmetros é utilizada apenas na mensagem exibida, contribuindo para a complexidade da interface do método.

## 5. Middle Man (Intermediário)

**Localização:** Método `middle_method()`.

**Trecho:**
```python
def middle_method(self):
    print("Middleman method delegating to another method")
    self.real_method()
```

**Justificativa:** O método atua principalmente como intermediário entre `middleman_method()` e `real_method()`, delegando a execução da funcionalidade a outro método, sem realizar processamento significativo além da exibição de uma mensagem.

## 6. Inappropriate Intimacy (Intimidade Inapropriada)

**Localização:** Método `access_internal_details()`.

**Trecho:**
```python
def access_internal_details(self):
    print(f"Accessing internal details: {self.chef.busy}")
```

**Justificativa:** A classe `Cashier` acessa diretamente o atributo `busy` do objeto `Chef`, demonstrando conhecimento sobre seu estado interno. Essa dependência dos detalhes de outra classe caracteriza um acoplamento excessivo.

## 7. Feature Envy (Inveja de Funcionalidade)

**Localização:** Método `calm_customer_down()`.

**Trecho:**
```python
def calm_customer_down(self):
    print("Cashier is calming the customer down.")
    self.chef.clean_kitchen()
```

**Justificativa:** O método, cuja responsabilidade aparente é acalmar o cliente, depende de uma operação pertencente à classe `Chef` e sem relação direta com sua finalidade. Isso sugere uma responsabilidade inadequadamente distribuída entre as classes.

## 8. Large Class (Classe Grande)

**Localização:** Classe `Cashier`.

**Trecho:** Conjunto de atributos e métodos da classe, especialmente `update_contact_info()`, `notify_for_promotion()`, `apply_discount()`, `handle_complaint()` e `take_order()`.

**Justificativa:** A classe concentra diversas responsabilidades, incluindo gerenciamento de pedidos, informações de contato, promoções, descontos, reclamações e comunicação com o cozinheiro. Essa diversidade de funcionalidades caracteriza uma classe com responsabilidades excessivas.

---

## Resumo da análise

| Code Smell | Localização |
|---|---|
| Data Clumps | `__init__()`, `update_contact_info()` |
| Temporary Field | `__init__()` |
| Dead Code | `another_unused_method()`, `yet_another_unused_method()`, `refused_bequest()` |
| Long Parameter List | `order_with_unnecessary_details()` |
| Middle Man | `middle_method()` |
| Inappropriate Intimacy | `access_internal_details()` |
| Feature Envy | `calm_customer_down()` |
| Large Class | Classe `Cashier` |

**Observação:** Alguns casos possuem evidências menos conclusivas. Em especial, *Temporary Field* não pode ser confirmado apenas pelo prefixo `temp_` e pela ausência de uso; *Feature Envy* também depende da distribuição real das responsabilidades.

O método `long_method()` não apresenta extensão suficiente para caracterizar claramente *Long Method*, e `chain_of_methods()` não contém uma cadeia de chamadas que caracterize *Message Chains*. Além disso, a repetição de chamadas em `duplicate_method()` não é, por si só, evidência suficiente de *Duplicated Code*.

A estrutura condicional de `handle_complaint()` é redundante, mas não foi contabilizada como *Repeated Switches*, pois não há repetição da mesma estrutura condicional em outros pontos do código.