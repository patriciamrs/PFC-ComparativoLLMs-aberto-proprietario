# Análise de Code Smells — Classe Customer (Java)

### 1. Long Parameter List (Lista Longa de Parâmetros)

- **Localização:** Método `orderWithUnnecessaryDetails()`.
- **Trecho:**
  `orderWithUnnecessaryDetails(String pizzaType, String size, String crustType, String toppings, boolean extraCheese, String discountCode)`
- **Justificativa:** O método recebe seis parâmetros, tornando sua assinatura extensa e aumentando a complexidade de utilização. Além disso, grande parte das informações recebidas é utilizada somente na mensagem impressa, sem participar efetivamente do processamento do pedido.

### 2. Message Chains (Cadeias de Mensagens)

- **Localização:** Métodos `chainOfMethods()` e `accessInternalDetails()`.
- **Trechos:**
  - `this.pizzaShop.getCashier().getChef().cleanKitchen();`
  - `pizzaShop.getCashier().getChef().isBusy();`
- **Justificativa:** Os métodos realizam chamadas encadeadas para acessar objetos internos de outros objetos. A classe `Customer` precisa conhecer a estrutura de relacionamento entre `Shop`, `Cashier` e `Chef`, aumentando o acoplamento entre as classes.

### 3. Middle Man (Intermediário)

- **Localização:** Método `middleMethod()`.
- **Trecho:** `this.realMethod();`
- **Justificativa:** O método atua como intermediário entre `middlemanMethod()` e `realMethod()`, delegando a execução principal para outro método. Embora imprima uma mensagem, não acrescenta processamento relevante ao comportamento delegado.

### 4. Dead Code (Código Morto)

- **Localização:** Métodos `anotherUnusedMethod()` e `refusedBequest()`.
- **Trechos:**
  - `public void anotherUnusedMethod() {}`
  - `public void refusedBequest() {}`
- **Justificativa:** Ambos os métodos possuem corpos vazios, sem implementar qualquer comportamento. São candidatos a código morto, embora não seja possível confirmar que nunca são utilizados sem examinar as demais classes do sistema.

### 5. Duplicate Code (Código Duplicado)

- **Localização:** Método `duplicateComplaint()`.
- **Trecho:**
  - `this.complain("Pizza is cold");` — repetido duas vezes.
  - `this.complain("Pizza is late");` — repetido duas vezes.
- **Justificativa:** O método contém chamadas idênticas repetidas consecutivamente, resultando em duplicação explícita de instruções que executam exatamente a mesma operação.

### 6. Large Class (Classe Grande)

- **Localização:** Classe `Customer`.
- **Trecho:** Conjunto de métodos da classe, especialmente `orderPizza()`, `handleComplaint()`, `notifyForPromotion()`, `applyDiscount()`, `applyLoyaltyPoints()` e `updateContactInfo()`.
- **Justificativa:** A classe concentra diversas responsabilidades, incluindo pedidos, reclamações, atualização de dados pessoais, notificações e benefícios. Essa diversidade de comportamentos aumenta sua complexidade e dificulta sua manutenção. A quantidade de métodos, isoladamente, não determina o smell; o principal indício é a concentração de responsabilidades distintas.

### 7. Data Clumps (Agrupamentos de Dados)

- **Localização:** Atributos de contato e métodos `updateContactInfo()` e `updateName()`.
- **Trechos:**
  - `firstName`
  - `lastName`
  - `address`
  - `phoneNumber`
  - `email`
- **Justificativa:** Os dados pessoais e de contato aparecem agrupados tanto nos atributos quanto nos parâmetros do método de atualização. Essa repetição de um conjunto de informações relacionadas caracteriza um indício de Data Clumps.

### 8. Switch Statements / Repeated Switches (Condicionais por Tipo)

- **Localização:** Método `handleComplaint()`.
- **Trecho:** Estrutura `if / else if / else` que verifica os valores `"cold pizza"`, `"late delivery"` e `"wrong order"`.
- **Justificativa:** O método utiliza uma sequência de condições para determinar o comportamento com base no tipo de reclamação representado por uma string. Entretanto, uma única estrutura condicional não é suficiente para confirmar o smell Repeated Switches descrito por Fowler; seria necessário observar a repetição dessa lógica em diferentes pontos do sistema.

### 9. Temporary Field (Campo Temporário)

- **Localização:** Atributos `tempDiscountCode` e `tempOrderNote`.
- **Trechos:**
  - `private String tempDiscountCode;`
  - `private String tempOrderNote;`
- **Justificativa:** Os atributos possuem nomes que indicam armazenamento temporário, mas não são inicializados ou utilizados nos métodos apresentados. Isso sugere a existência de campos sem uma função permanente na classe. A caracterização como Temporary Field, porém, depende de evidências de que sejam utilizados apenas em determinadas circunstâncias.

---

## Resumo da Análise

| Code Smell | Localização | Avaliação |
|---|---|---|
| Long Parameter List | `orderWithUnnecessaryDetails()` | Identificado |
| Message Chains | `chainOfMethods()`, `accessInternalDetails()` | Identificado |
| Middle Man | `middleMethod()` | Indício |
| Dead Code | `anotherUnusedMethod()`, `refusedBequest()` | Indício |
| Duplicate Code | `duplicateComplaint()` | Identificado |
| Large Class | Classe `Customer` | Identificado |
| Data Clumps | Dados de contato | Indício |
| Repeated Switches | `handleComplaint()` | Não confirmado |
| Temporary Field | `tempDiscountCode`, `tempOrderNote` | Não confirmado |

**Observação:** Não foram identificados elementos suficientes para classificar `refusedBequest()` como Refused Bequest, pois esse smell está relacionado a estruturas de herança, inexistentes no código apresentado. Também não há evidências suficientes para afirmar que `longComplaintMethod()` caracteriza Long Method, considerando seu tamanho e sua complexidade relativamente reduzidos.
