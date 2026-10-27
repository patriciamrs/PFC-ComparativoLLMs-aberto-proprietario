# Análise de Code Smells — Classe `Chef`

Abaixo estão listados os code smells identificados no código, com o local de ocorrência e a justificativa.

---

**1. Código Morto (Dead Code)**

- **Onde:** `anotherUnusedMethod()`, `yetAnotherUnusedMethod()`, `refusedBequest()`
- **Justificativa:** São métodos vazios, sem corpo e sem qualquer chamada que os invoque. Não exercem nenhuma função no sistema e nunca são executados, caracterizando código morto.

---

**2. Método Longo (Long Method)**

- **Onde:** `longMethod()`
- **Justificativa:** O método concentra um grande número de instruções (dezoito chamadas), invocando funcionalidades das mais diversas (bake, cut, deliver, clean, update, notify, apply, handle, ask, chain, middle, access). Isso o torna extenso, de difícil leitura e com responsabilidades múltiplas.

---

**3. Código Duplicado (Duplicated Code)**

- **Onde:** `duplicateMethod()`
- **Justificativa:** O método realiza duas chamadas idênticas `this.bakePizza("Cheese")` em sequência, ou seja, repete a mesma lógica sem qualquer variação, o que configura duplicação de código.

---

**4. Cadeia de Mensagens (Message Chains)**

- **Onde:** `longMethod()` → invoca `chainOfMethods()`
- **Justificativa:** A partir de `longMethod()` há uma sequência de invocações encadeadas (`longMethod → chainOfMethods → cleanKitchen`), na qual o cliente precisa navegar por uma cadeia de métodos para chegar à ação final. Isso caracteriza o chamado *message chain*.

---

**5. Classe Média / Intermediária (Middle Man)**

- **Onde:** `middlemanMethod()` e `middleMethod()`
- **Justificativa:** `middlemanMethod()` apenas delega para `middleMethod()`, e este, por sua vez, apenas delega para `realMethod()`. Os métodos intermediários não adicionam comportamento algum, servindo unicamente de passagem — o padrão típico de um *middle man*.

---

**6. Intimidade Inapropriada (Inappropriate Intimacy)**

- **Onde:** `accessInternalDetails()`
- **Justificativa:** O método acessa diretamente o detalhe interno de outro objeto por meio de `this.pizza.getTopping()`, expondo e consultando o estado interno da classe `Pizza`. Isso demonstra acoplamento excessivo entre as classes.

---

**7. Legitimação Incompleta / Recusa de Herança (Refused Bequest)**

- **Onde:** `refusedBequest()`
- **Justificativa:** O método está declarado mas possui corpo vazio, não aproveitando nem utilizando qualquer comportamento herdado ou esperado. É um típico caso de *refused bequest*, em que a subclasse (ou a classe em questão) ignora/recusa o que foi definido.

---

**8. Classe Grande (Large Class)**

- **Onde:** A própria classe `Chef`
- **Justificativa:** A classe possui muitos atributos (`pizza`, `busy`, `completedOrders`, `breaksTaken`, `kitchenClean`, `extraCheese`, `firstName`, `lastName`, `address`, `phoneNumber`, `email`, `tempDiscountCode`, `tempOrderNote`) e muitos métodos, misturando responsabilidades bem distintas: cozinhar pizza, gerenciar dados de contato do cliente, notificações de marketing, tratamento de reclamações, etc. Isso indica uma classe com excesso de responsabilidades.

---

**9. Campo Temporário / Variáveis Não Utilizadas**

- **Onde:** Atributos `tempDiscountCode` e `tempOrderNote`
- **Justificativa:** Os campos `tempDiscountCode` e `tempOrderNote` são declarados mas nunca inicializados nem utilizados em nenhum método. Isso indica campos temporários/redundantes que não têm propósito no estado do objeto.

---

**10. Lista Longa de Parâmetros (Long Parameter List)**

- **Onde:** `updateContactInfo(String firstName, String lastName, String address, String phoneNumber, String email)`
- **Justificativa:** O método recebe cinco parâmetros relacionados entre si (dados de contato). Uma quantidade elevada de parâmetros conjugados dificulta a legibilidade e a chamada do método, caracterizando *long parameter list*.

---

**11. Números/Booleans Mágicos / Flags (Boolean/Flag Parameters) — comportamento condicional frágil**

- **Onde:** Atributos `busy`, `kitchenClean`, `extraCheese` e método `handleComplaint(String complaint)`
- **Justificativa:** O método `handleComplaint()` utiliza uma cadeia de `if/else if` comparando strings literais ("cold pizza", "late delivery", "wrong order") sem qualquer abstração (ex.: enum), o que caracteriza *conditional complexity* / uso de valores literais mágicos. Além disso, o objeto carrega várias flags booleanas (`busy`, `kitchenClean`, `extraCheese`) que controlam estado interno, indicando *flag arguments/state flags*.

---

**12. Baixa Coesão (Low Cohesion / Divergent Change)**

- **Onde:** Toda a classe `Chef`
- **Justificativa:** Os métodos da classe tratam de assuntos completamente distintos — operações de cozinha (`bakePizza`, `cutPizzaAndPutInBox`, `deliverPizza`), dados pessoais (`updateName`, `updateAddress`, `updatePhoneNumber`, `updateEmail`), marketing (`notifyForPromotion`, `notifyForDiscount`, `notifyForNewArrivals`, `applyDiscount`, `applyLoyaltyPoints`) e atendimento ao cliente (`handleComplaint`, `askForReceipt`). Essa mistura de responsabilidades não relacionadas indica baixa coesão e tendência a divergir por vários motivos de mudança.

---

**13. Métodos com Nome Pouco Significativo / Métodos de Teste (Dead/Placeholder Methods)**

- **Onde:** `anotherUnusedMethod()`, `yetAnotherUnusedMethod()`, `longMethod()`, `duplicateMethod()`
- **Justificativa:** Os nomes `anotherUnusedMethod`, `yetAnotherUnusedMethod`, `longMethod`, `duplicateMethod` são claramente placeholders que descrevem o próprio defeito e não a intenção do código. Esses métodos foram inseridos sem propósito funcional (reforçando o item de *dead code*), mas, se executados, só imprimem mensagens genéricas — indício de código artificial para estudo de smells.

---

## Resumo dos Smells Encontrados

| # | Code Smell | Local |
|---|------------|-------|
| 1 | Dead Code | `anotherUnusedMethod`, `yetAnotherUnusedMethod`, `refusedBequest` |
| 2 | Long Method | `longMethod()` |
| 3 | Duplicated Code | `duplicateMethod()` |
| 4 | Message Chains | `longMethod()` → `chainOfMethods()` |
| 5 | Middle Man | `middlemanMethod()`, `middleMethod()` |
| 6 | Inappropriate Intimacy | `accessInternalDetails()` |
| 7 | Refused Bequest | `refusedBequest()` |
| 8 | Large Class | classe `Chef` |
| 9 | Campos Não Utilizados / Temporários | `tempDiscountCode`, `tempOrderNote` |
| 10 | Long Parameter List | `updateContactInfo(...)` |
| 11 | Conditionais complexos / Flags | `handleComplaint()`, flags `busy`, `kitchenClean`, `extraCheese` |
| 12 | Low Cohesion / Divergent Change | classe `Chef` (todo) |
| 13 | Nomes pouco significativos / placeholders | métodos com nomes descritivos do defeito |

> Observação: conforme solicitado, a análise se limita a **identificar** os smells existentes, sem propor refatorações ou alterações no código.