# Análise de Code Smells — Cashier.java

### 1. Large Class (Classe Grande)
- **Localização:** Classe `Cashier`.
- **Justificativa:** A classe concentra diversas responsabilidades, incluindo gerenciamento de pedidos, comunicação com o chef, atendimento ao cliente, atualização de informações pessoais, aplicação de descontos e envio de notificações. Essa variedade de responsabilidades indica que a classe acumula funcionalidades de diferentes contextos.

### 2. Long Parameter List (Lista Longa de Parâmetros)
- **Localização:** Método `updateContactInfo()`.
- **Trecho:** `updateContactInfo(String firstName, String lastName, String address, String phoneNumber, String email)`.
- **Justificativa:** O método recebe cinco parâmetros relacionados aos dados de contato do cliente, caracterizando uma lista extensa de argumentos e aumentando a quantidade de informações necessárias para sua utilização.

### 3. Data Clumps (Agrupamento de Dados)
- **Localização:** Atributos `firstName`, `lastName`, `address`, `phoneNumber` e `email`, utilizados nos métodos `updateContactInfo()` e `updateName()`.
- **Justificativa:** Os atributos representam informações relacionadas ao cliente e são manipulados em conjunto. A associação entre esses dados indica um agrupamento que possui significado próprio.

### 4. Dead Code (Código Morto)
- **Localização:** Métodos `anotherUnusedMethod()` e `refusedBequest()`.
- **Justificativa:** Os métodos possuem corpos vazios e não executam nenhuma operação. Também não apresentam chamadas no código fornecido, indicando funcionalidades sem implementação útil. Entretanto, não é possível confirmar se são utilizados por outras classes.

### 5. Middle Man (Intermediário)
- **Localização:** Métodos `middlemanMethod()` e `middleMethod()`.
- **Justificativa:** Os métodos atuam principalmente como intermediários, encaminhando a execução para outros métodos sem acrescentar lógica significativa além das mensagens exibidas.

### 6. Temporary Field (Campo Temporário)
- **Localização:** Atributos `tempDiscountCode` e `tempOrderNote`.
- **Justificativa:** Os atributos são declarados, mas não são utilizados nos métodos apresentados. Seus nomes sugerem informações temporárias, embora o código não permita confirmar que sejam utilizados somente em determinadas circunstâncias.

### 7. Switch Statements / Repeated Conditional Logic (Lógica Condicional Repetida)
- **Localização:** Método `handleComplaint()`.
- **Justificativa:** O método apresenta uma sequência de condições que executam exatamente a mesma operação, independentemente da reclamação recebida. Isso caracteriza uma estrutura condicional redundante e desnecessariamente complexa.

### 8. Duplicate Code (Código Duplicado)
- **Localização:** Método `handleComplaint()`.
- **Trecho:** Chamada `this.calmCustomerDown()` repetida nos quatro caminhos condicionais.
- **Justificativa:** A mesma operação aparece em todas as condições do método, representando uma duplicação explícita de comportamento.

### 9. Inappropriate Intimacy (Intimidade Inadequada)
- **Localização:** Método `accessInternalDetails()`.
- **Trecho:** `chef.isBusy()`.
- **Justificativa:** A classe `Cashier` consulta diretamente o estado operacional do objeto `Chef`, demonstrando conhecimento sobre informações de outra classe. Isso pode indicar um acoplamento entre responsabilidades distintas, embora o uso de um método público não seja suficiente, isoladamente, para confirmar o smell.

---

### Observação
Os smells **Dead Code**, **Temporary Field** e **Inappropriate Intimacy** apresentam indícios, mas não podem ser confirmados integralmente apenas com o código fornecido. Os demais possuem evidências mais diretas na implementação.
