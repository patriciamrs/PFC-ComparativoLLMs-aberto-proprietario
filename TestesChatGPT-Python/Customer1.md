
# Análise de Code Smells — Classe `Customer` (Python)

## 1. Large Class (Classe Grande)

- **Localização:** Classe `Customer`.
- **Justificativa:** A classe possui diversos atributos e métodos que abrangem responsabilidades diferentes, como realização de pedidos, gerenciamento de informações de contato, notificações promocionais, descontos e tratamento de reclamações. Essa concentração de funcionalidades torna a classe extensa e com múltiplas responsabilidades.

## 2. Long Method (Método Longo)

- **Localização:** Método `long_complaint_method()`.
- **Justificativa:** O método reúne diversas chamadas consecutivas para registrar reclamações diferentes, além de solicitar um recibo. Embora não seja muito extenso em número de linhas, concentra várias operações em uma única sequência, caracterizando um possível método com responsabilidades excessivas.

## 3. Long Parameter List (Lista Longa de Parâmetros)

- **Localização:** Método `update_contact_info()`.
- **Justificativa:** O método recebe cinco parâmetros (`first_name`, `last_name`, `address`, `phone_number` e `email`) para atualizar as informações do cliente. A quantidade de parâmetros aumenta a complexidade da chamada e exige o fornecimento de vários dados relacionados.

## 4. Data Clumps (Agrupamentos de Dados)

- **Localização:** Atributos `first_name`, `last_name`, `address`, `phone_number` e `email`, além do método `update_contact_info()`.
- **Justificativa:** Os atributos representam informações de contato que aparecem agrupadas tanto na inicialização da classe quanto nos parâmetros do método. Esse conjunto de dados possui uma relação lógica e é manipulado em conjunto.

## 5. Primitive Obsession (Obsessão por Tipos Primitivos)

- **Localização:** Atributos `frequent_customer_discount`, `first_name`, `last_name`, `address`, `phone_number`, `email` e `temp_discount_code`.
- **Justificativa:** O código representa informações relacionadas ao cliente, contatos e descontos por meio de valores primitivos, como strings e booleanos, sem utilizar estruturas específicas para representar esses conceitos e seus comportamentos.

## 6. Message Chains (Cadeia de Mensagens)

- **Localização:** Métodos `complain()`, `chain_of_methods()` e `access_internal_details()`.
- **Trechos:**

```python
self.pizza_shop.casher.calm_customer_down()
self.pizza_shop.casher.chef.clean_kitchen()
```

```python
self.pizza_shop.casher.chef.clean_kitchen()
```

```python
self.pizza_shop.casher.chef.busy
```

- **Justificativa:** Os métodos acessam objetos por meio de cadeias sucessivas de atributos, passando de `pizza_shop` para `casher` e depois para `chef`. Isso cria dependências entre a classe `Customer` e a estrutura interna de outros objetos.

## 7. Inappropriate Intimacy (Intimidade Inapropriada)

- **Localização:** Métodos `complain()`, `chain_of_methods()` e `access_internal_details()`.
- **Justificativa:** A classe `Customer` acessa diretamente detalhes internos de objetos associados à loja, incluindo o objeto `chef` e seu atributo `busy`. Esse conhecimento da estrutura interna de outras classes aumenta o acoplamento e caracteriza uma relação excessivamente próxima entre os componentes.

## 8. Duplicate Code (Código Duplicado)

- **Localização:** Método `duplicate_complaint()`.
- **Trecho:**

```python
self.complain("Pizza is cold")
self.complain("Pizza is cold")
self.complain("Pizza is late")
self.complain("Pizza is late")
```

- **Justificativa:** O método apresenta chamadas idênticas repetidas consecutivamente, realizando as mesmas operações para as mesmas reclamações. Essa repetição introduz redundância no código, embora a intenção de registrar reclamações repetidas não possa ser descartada.

## 9. Middle Man (Intermediário)

- **Localização:** Métodos `middleman_method()` e `middle_method()`.
- **Trecho:**

```python
def middleman_method(self):
    print("Customer is calling a middleman method")
    self.middle_method()

def middle_method(self):
    print("Middleman method delegating to another method")
    self.real_method()
```

- **Justificativa:** Os métodos atuam como intermediários entre chamadas, encaminhando a execução até `real_method()` sem adicionar lógica significativa além de mensagens informativas. Essa estrutura introduz níveis de delegação com pouca funcionalidade própria.

## 10. Lazy Element (Elemento Preguiçoso)

- **Localização:** Métodos `middleman_method()` e `middle_method()`.
- **Justificativa:** Os métodos possuem implementações simples e praticamente se limitam a chamar outros métodos. A baixa quantidade de comportamento próprio não justifica claramente a existência dessas estruturas intermediárias.

## 11. Divergent Change (Mudança Divergente)

- **Localização:** Classe `Customer`.
- **Justificativa:** A classe concentra funcionalidades relacionadas a pedidos, reclamações, informações pessoais, notificações e descontos. Alterações em qualquer uma dessas áreas podem exigir modificações na mesma classe, indicando diferentes motivos para mudança.

## 12. Dead Code (Código Morto)

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

- **Justificativa:** Os métodos apresentam apenas a instrução `pass`, sem executar qualquer operação. São implementações vazias e não possuem funcionalidade observável no código apresentado. Entretanto, sua ausência de uso no restante do sistema não pode ser confirmada.

## 13. Speculative Generality (Generalidade Especulativa)

- **Localização:** Métodos `another_unused_method()`, `yet_another_unused_method()` e `refused_bequest()`.
- **Justificativa:** Os métodos são declarados sem implementação funcional e não demonstram uma necessidade concreta no trecho analisado. Podem representar funcionalidades previstas antecipadamente, embora essa intenção não possa ser confirmada apenas pelo código.

## 14. Temporary Field (Campo Temporário)

- **Localização:** Atributos `temp_discount_code` e `temp_order_note`, declarados em `__init__()`.
- **Justificativa:** Os campos são inicializados com `None` e não aparecem nas operações realizadas pelos métodos da classe. Seus nomes indicam dados temporários, mas não há evidências suficientes de que sejam utilizados somente em circunstâncias específicas, como exige a caracterização desse *code smell*.

---

## Considerações sobre a identificação

Os *code smells* com evidências mais claras são **Large Class, Long Parameter List, Data Clumps, Message Chains, Inappropriate Intimacy, Middle Man, Lazy Element e Divergent Change**.

A identificação de *Long Method*, *Duplicate Code*, *Primitive Obsession*, *Dead Code*, *Speculative Generality* e *Temporary Field* exige maior cautela, pois algumas características observadas não são suficientes, isoladamente, para confirmar essas classificações.

Além disso, o método `order_with_unnecessary_details()` contém uma chamada para `order_pizza()` com 20 argumentos, enquanto `order_pizza()` aceita apenas um argumento além de `self`. Isso representa um erro de chamada de método que provocaria um `TypeError`, e não uma ocorrência de *Long Parameter List*, pois o método declarado não possui uma lista extensa de parâmetros.

O método `refused_bequest()` também não caracteriza *Refused Bequest*, uma vez que a classe `Customer` não apresenta uma relação de herança no código fornecido.
