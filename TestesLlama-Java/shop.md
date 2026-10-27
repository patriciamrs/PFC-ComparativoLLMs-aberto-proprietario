# Análise de Code Smells — Classe `Shop`

## 1. Classe Deus (God Class / Large Class)

**Ocorrência:** Classe `Shop` inteira.

**Justificativa:** A classe centraliza responsabilidades muito distintas — criação de pizzas (`createPizza`), gestão de dados de contato do cliente (`firstName`, `lastName`, `address`, `phoneNumber`, `email`), notificações (`notifyForPromotion`, `notifyForDiscount`, `notifyForNewArrivals`), aplicação de benefícios (`applyDiscount`, `applyLoyaltyPoints`) e tratamento de reclamações (`handleComplaint`). Ela acumula responsabilidades que não lhe pertencem, configurando uma classe "faz-tudo".

---

## 2. Feature Envy (Inveja de Funcionalidade)

**Ocorrência:** Métodos `handleComplaint`, `notifyForPromotion`, `notifyForDiscount`, `notifyForNewArrivals`, `applyDiscount`, `applyLoyaltyPoints`.

**Justificativa:** Esses comportamentos pertencem conceitualmente a outras classes (respectivamente `Cashier`/`Customer`), e não à `Shop`. O método `handleComplaint`, por exemplo, apenas delega sempre para `cashier.calmCustomerDown()`, ou seja, a lógica reside no `Cashier`, mas está exposta indevidamente pela `Shop`.

---

## 3. Número Mágico de Parâmetros / Lista de Parâmetros Longa (Long Parameter List)

**Ocorrência:** Método `updateContactInfo(String firstName, String lastName, String address, String phoneNumber, String email)`.

**Justificativa:** O método recebe cinco parâmetros individuais que representam um agrupamento coeso de dados do cliente (informações de contato), o que caracteriza lista de parâmetros excessivamente longa.

---

## 4. Dados Agrupados / Grupo de Dados (Data Clumps)

**Ocorrência:** Campos `firstName`, `lastName`, `address`, `phoneNumber`, `email` (e também os parâmetros de `updateContactInfo` e de `updateName`).

**Justificativa:** Esses campos quase sempre aparecem juntos e representam um conceito único (dados de contato do cliente). Ficam repetidamente agrupados em campos e assinaturas, evidenciando um "grupamento de dados".

---

## 5. Obsessão Primitiva (Primitive Obsession)

**Ocorrência:** Campos `String firstName`, `lastName`, `address`, `phoneNumber`, `email`; e o parâmetro `String pizzaType`.

**Justificativa:** Conceitos de domínio que mereceriam tipos próprios (ex.: dados de contato, um tipo `PizzaType`/enum) são representados apenas por `String` primitivas, sem qualquer encapsulamento ou validação.

---

## 6. Cadeia de Condicionais / Muitos `if-else` (Switch/If-Else Ladder)

**Ocorrência:** Métodos `createPizza(String pizzaType)` e `handleComplaint(String complaint)`.

**Justificativa:** Ambos usam longas cadeias de `if-else if` para despachar por tipo/string. Em `createPizza` há uma cascata de quatro verificações; em `handleComplaint` há três ramos que executam exatamente a mesma ação. Essas cadeias tornam o código prolixo e de difícil manutenção.

---

## 7. Código Morto com Estrutura Redundante (Duplicated Code Branches / Dead Conditional)

**Ocorrência:** Método `handleComplaint(String complaint)`.

**Justificativa:** Todos os quatro ramos (`cold pizza`, `late delivery`, `wrong order` e o `else`) executam a mesma instrução `cashier.calmCustomerDown()`. As condições não produzem comportamento distinto, caracterizando ramificações redundantes e código essencialmente morto (a estrutura condicional não tem efeito).

---

## 8. Método Morto / Código Não Utilizado (Dead Code)

**Ocorrência:** Método `anotherUnusedMethod()`.

**Justificativa:** O próprio nome declara e o corpo vazio confirma: método que não possui implementação e não é invocado, constituindo código morto.

---

## 9. Campos Não Utilizados (Dead Code / Unused Fields)

**Ocorrência:** Campos `tempDiscountCode` e `tempOrderNote`.

**Justificativa:** São declarados mas nunca atribuídos nem lidos em nenhum método da classe, configurando campos mortos.

---

## 10. Variável / Campo Temporário Mal Utilizado (Temporary Field)

**Ocorrência:** Campos `tempDiscountCode` e `tempOrderNote` (pelo prefixo "temp").

**Justificativa:** O prefixo "temp" sugere campos usados apenas em circunstâncias específicas, e no caso estão sequer em uso — reforçando a caracterização de campos temporários que deveriam ser locais ou inexistentes.

---

## 11. Exposição de Estrutura Interna / Métodos de Acesso Desnecessários (Inappropriate Intimacy / Feature Chain)

**Ocorrência:** Métodos `getChef()` e `getCashier()`.

**Justificativa:** Expor `Chef` e `Cashier` internos permite que outras classes manipulem diretamente os colaboradores internos da `Shop`, quebrando o encapsulamento e criando acoplamento indevido entre classes.

---

## 12. Setters Fragmentados / Métodos de Atualização Trivial (repetitivos e redundantes)

**Ocorrência:** Métodos `updateName`, `updateAddress`, `updatePhoneNumber`, `updateEmail` em conjunto com `updateContactInfo`.

**Justificativa:** Há sobreposição de responsabilidades: `updateContactInfo` já atualiza todos os dados, tornando os demais métodos de atualização parciais duplicados/redundantes entre si — comportamento duplicado de atribuição.

---

## 13. Comparação com `equals` em String Literal (String Comparison / Possível NPE)

**Ocorrência:** `createPizza`: `pizzaType.equals("Cheese")`; `handleComplaint`: `complaint.equals("cold pizza")`.

**Justificativa:** Invocar `.equals` diretamente sobre o parâmetro pode lançar `NullPointerException` se o argumento for nulo, além de representar comparação frágil baseada em strings literais para tomada de decisão de fluxo (relaciona-se à Obsessão Primitiva e Stubs de string).

---

## 14. Baixa Coesão (Low Cohesion)

**Ocorrência:** Classe `Shop`.

**Justificativa:** Os métodos tratam de preocupações heterogêneas (criação de objetos, dados de cliente, notificações, benefícios, reclamações, recibo), indicando que a classe agrupa funcionalidades que não pertencem logicamente juntas.

---

## 15. Inveja de Comportamento de `Cashier` via Delegation Excessiva / Middle Man

**Ocorrência:** Métodos `handleComplaint`, `notifyFor*`, `applyDiscount`, `applyLoyaltyPoints`.

**Justificativa:** Vários métodos da `Shop` funcionam apenas como repasse (delegação) para o `Cashier` ou imprimem mensagens triviais, atuando como "intermediários" sem agregação de valor próprio — caracterizando uma classe que se comporta parcialmente como *Middle Man*.

---

**Resumo:** O código concentra principalmente sintomas de **God Class**, **Feature Envy**, **dados/parâmetros agrupados**, **obsessão primitiva**, **cadeias condicionais redundantes com código morto**, **campos e métodos não utilizados** e **baixa coesão com delegação excessiva**.