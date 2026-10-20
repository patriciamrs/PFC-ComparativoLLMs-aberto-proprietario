
# Análise de Code Smells — Classe Shop

### 1. Primitive Obsession (Obsessão por Tipos Primitivos)

**Localização:**
- Atributo `frequentCustomerDiscount`.
- Parâmetro `pizzaType` do método `createPizza()`.
- Parâmetro `complaint` do método `handleComplaint()`.

**Justificativa:**

O atributo `frequentCustomerDiscount` utiliza um valor booleano para representar uma condição de desconto. Além disso, os métodos `createPizza()` e `handleComplaint()` utilizam strings para representar categorias específicas de pizzas e reclamações, respectivamente. Essas informações são tratadas por meio de tipos primitivos e comparações com valores literais, caracterizando o uso excessivo de tipos primitivos para representar conceitos do domínio.

### 2. Data Clumps (Agrupamento de Dados)

**Localização:**
- Atributos `firstName`, `lastName`, `address`, `phoneNumber` e `email`.
- Parâmetros do método `updateContactInfo()`.

**Justificativa:**

Os atributos representam um conjunto de informações relacionadas aos dados pessoais e de contato. Esses mesmos dados aparecem agrupados nos parâmetros do método `updateContactInfo()`, evidenciando a presença de um conjunto de informações que são utilizadas em conjunto.

### 3. Temporary Field (Campo Temporário)

**Localização:**
- Atributos `tempDiscountCode` e `tempOrderNote`.

**Justificativa:**

Os atributos indicam informações temporárias relacionadas a descontos e observações de pedidos. Entretanto, não são inicializados nem utilizados nos métodos apresentados, permanecendo sem uma função definida no comportamento da classe. Isso sugere a presença de campos que não participam do estado habitual do objeto.

### 4. Long Parameter List (Lista Longa de Parâmetros)

**Localização:**
- Método `updateContactInfo(String firstName, String lastName, String address, String phoneNumber, String email)`.

**Justificativa:**

O método recebe cinco parâmetros individuais relacionados às informações pessoais e de contato. A quantidade de argumentos aumenta a complexidade da assinatura e caracteriza uma lista extensa de parâmetros.

### 5. Switch Statements (Estruturas Condicionais Repetitivas)

**Localização:**
- Método `createPizza()`.

**Justificativa:**

O método utiliza uma sequência de condições `if/else if` para verificar o tipo de pizza informado e instanciar uma classe específica. Essa estrutura concentra a seleção de diferentes comportamentos com base em valores literais de uma string, caracterizando uma estrutura condicional de seleção de tipos.

### 6. Duplicate Code (Código Duplicado)

**Localização:**
- Método `handleComplaint()`.

**Justificativa:**

Todas as condições do método executam exatamente a mesma instrução, `cashier.calmCustomerDown()`, independentemente do tipo de reclamação recebido. Isso representa uma duplicação explícita de código nos diferentes ramos condicionais.

### 7. Lazy Element (Elemento Desnecessário)

**Localização:**
- Método `anotherUnusedMethod()`.

**Justificativa:**

O método possui implementação vazia e não apresenta nenhuma funcionalidade. Sua existência não acrescenta comportamento à classe, caracterizando um elemento sem responsabilidade efetiva.

### 8. Large Class (Classe Grande)

**Localização:**
- Classe `Shop`.

**Justificativa:**

A classe concentra diferentes responsabilidades, incluindo gerenciamento de pedidos, criação de pizzas, atualização de informações de contato, notificações promocionais, aplicação de benefícios e tratamento de reclamações. Essa variedade de funcionalidades indica uma concentração excessiva de responsabilidades em uma única classe.

### 9. Divergent Change (Mudança Divergente)

**Localização:**
- Classe `Shop`, especialmente nos métodos `receiveOrder()`, `createPizza()`, `updateContactInfo()`, `notifyForPromotion()`, `applyDiscount()` e `handleComplaint()`.

**Justificativa:**

A classe reúne funcionalidades pertencentes a diferentes áreas do sistema. Alterações nas regras de criação de pizzas, dados de contato, promoções ou reclamações podem exigir modificações na mesma classe por motivos distintos, indicando diferentes razões para mudança.

---

## Resumo dos Code Smells Identificados

| Code Smell | Localização |
|---|---|
| Primitive Obsession | `frequentCustomerDiscount`, `createPizza()`, `handleComplaint()` |
| Data Clumps | Atributos de contato e `updateContactInfo()` |
| Temporary Field | `tempDiscountCode`, `tempOrderNote` |
| Long Parameter List | `updateContactInfo()` |
| Switch Statements | `createPizza()` |
| Duplicate Code | `handleComplaint()` |
| Lazy Element | `anotherUnusedMethod()` |
| Large Class | `Shop` |
| Divergent Change | `Shop` |

**Observação:** Algumas classificações exigem cautela. Em particular, `Temporary Field` não fica plenamente comprovado apenas pela existência de atributos não utilizados; `Lazy Element` não comprova que o método esteja sem uso externo; e `Divergent Change` representa um indício estrutural, pois não há histórico de alterações disponível. Da mesma forma, um booleano isolado não é suficiente, por si só, para caracterizar `Primitive Obsession`. Essas distinções são importantes para evitar falsos positivos na identificação dos code smells.
