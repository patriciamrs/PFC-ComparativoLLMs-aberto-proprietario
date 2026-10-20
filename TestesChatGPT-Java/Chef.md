
# Análise de Code Smells — Classe `Chef`

A análise do código-fonte da classe `Chef`, com base nos *code smells* descritos por Martin Fowler no livro *Refatoração: Aperfeiçoando o Design de Códigos Existentes*, permitiu identificar as seguintes ocorrências.

### 1. Large Class (Classe Grande)

**Localização:** Classe `Chef`.

**Justificativa:** A classe concentra diferentes responsabilidades, incluindo preparação de pizzas, limpeza da cozinha, gerenciamento de informações de contato, notificações promocionais, descontos, reclamações e pedidos. Essa diversidade de funcionalidades caracteriza uma classe com responsabilidades excessivas.

### 2. Long Method (Método Longo)

**Localização:** Método `longMethod()`.

**Justificativa:** O método realiza uma sequência extensa de operações relacionadas a diferentes responsabilidades, como preparar pizzas, atualizar informações de contato, aplicar descontos e tratar reclamações. A concentração dessas operações em um único método dificulta a compreensão de seu propósito.

### 3. Data Clumps (Agrupamento de Dados)

**Localização:** Atributos `firstName`, `lastName`, `address`, `phoneNumber` e `email`, utilizados em conjunto no método `updateContactInfo()`.

**Justificativa:** Os atributos representam um conjunto de informações relacionadas ao contato de uma pessoa e aparecem agrupados tanto na declaração dos campos quanto nos parâmetros do método, caracterizando um agrupamento recorrente de dados.

### 4. Primitive Obsession (Obsessão por Tipos Primitivos)

**Localização:** Método `handleComplaint(String complaint)`.

**Justificativa:** O método utiliza uma `String` para representar diferentes tipos de reclamações, identificados por valores literais como `"cold pizza"`, `"late delivery"` e `"wrong order"`. Isso caracteriza o uso de um tipo primitivo para representar um conceito específico do domínio.

### 5. Temporary Field (Campo Temporário)

**Localização:** Atributos `tempDiscountCode` e `tempOrderNote`.

**Justificativa:** Os campos são declarados na classe, mas não são inicializados ou utilizados por nenhum método apresentado. Embora seus nomes indiquem informações temporárias, o código não demonstra que sejam utilizados apenas em determinadas circunstâncias, condição necessária para confirmar esse *code smell*.

### 6. Divergent Change (Mudança Divergente)

**Localização:** Classe `Chef`, especialmente os métodos `bakePizza()`, `cleanKitchen()`, `updateContactInfo()`, `notifyForPromotion()`, `applyDiscount()` e `handleComplaint()`.

**Justificativa:** A classe reúne funcionalidades de áreas distintas. Assim, mudanças nas regras de preparação de pizzas, nas informações de contato, nas promoções ou no tratamento de reclamações podem exigir modificações na mesma classe por motivos diferentes.

### 7. Shotgun Surgery (Cirurgia com Espingarda)

**Localização:** Não há ocorrência comprovada no código apresentado.

**Justificativa:** Esse *code smell* exige evidência de que uma única alteração provoque pequenas modificações em várias classes ou métodos dispersos. O código isolado da classe `Chef` não demonstra esse comportamento.

### 8. Middle Man (Intermediário)

**Localização:** Métodos `middlemanMethod()` e `middleMethod()`.

**Justificativa:** Esses métodos atuam principalmente como intermediários, encaminhando chamadas para outros métodos. `middlemanMethod()` chama `middleMethod()`, que, por sua vez, chama `realMethod()`, acrescentando apenas mensagens no console, sem uma responsabilidade funcional significativa.

### 9. Dead Code (Código Morto)

**Localização:** Métodos `anotherUnusedMethod()`, `yetAnotherUnusedMethod()` e `refusedBequest()`.

**Justificativa:** Os três métodos possuem implementações vazias e não são chamados por nenhum outro método da classe apresentada. Não desempenham nenhuma operação observável no código analisado.

Também se destacam os atributos `completedOrders`, `breaksTaken` e `extraCheese`, que recebem valores no construtor, mas não são posteriormente utilizados no trecho fornecido.

### 10. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Método `updateContactInfo(String firstName, String lastName, String address, String phoneNumber, String email)`.

**Justificativa:** O método recebe cinco parâmetros individuais relacionados a informações de contato. A quantidade de argumentos e a relação existente entre eles tornam a assinatura mais extensa e caracterizam uma lista longa de parâmetros.

---

## Observações sobre ocorrências não confirmadas

Alguns trechos apresentam nomes sugestivos, mas não fornecem evidências suficientes para identificar outros *code smells* de Fowler:

- **Duplicated Code:** o método `duplicateMethod()` chama `bakePizza("Cheese")` duas vezes, mas a repetição de uma chamada não constitui necessariamente duplicação de implementação.
- **Message Chains:** o encadeamento entre `middlemanMethod()`, `middleMethod()` e `realMethod()` não caracteriza uma cadeia de mensagens no sentido descrito por Fowler, pois não há navegação sucessiva entre objetos.
- **Inappropriate Intimacy:** `accessInternalDetails()` utiliza o método público `getTopping()` de `Pizza`, sem evidenciar acesso excessivo aos detalhes internos de outra classe.
- **Feature Envy:** o uso isolado de `pizza.getTopping()` não é suficiente para demonstrar que um método depende excessivamente dos dados de outra classe.
- **Refused Bequest:** a classe `Chef` não apresenta herança, portanto o método `refusedBequest()` não demonstra esse *code smell*.
- **Temporary Field:** os atributos com prefixo `temp` não comprovam, por si só, uma utilização temporária.

**Conclusão:** Os *code smells* com evidências mais claras no código são **Large Class, Long Method, Data Clumps, Primitive Obsession, Divergent Change, Middle Man, Dead Code e Long Parameter List**. Os demais casos mencionados exigiriam informações adicionais para serem confirmados.
