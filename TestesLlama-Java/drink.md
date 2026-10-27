# Análise de Code Smells — Classe `Drink`

Abaixo estão os code smells presentes no código. Cada item apresenta a classe/método afetado, o trecho relevante e a justificativa.

---

## 1. God Class (Blob / Classe Deus)

**Onde:** Classe `Drink` inteira.

**Trecho:**
```java
public class Drink {
    private String drinkType;
    private boolean isLargeSize;
    private String customerFirstName;
    private String customerLastName;
    private String customerAddress;
    private String customerPhoneNumber;
    private String customerEmail;
    private String tempDiscountCode;
    private String tempOrderNote;
    ...
}
```

**Justificativa:** A classe `Drink`, que deveria representar apenas uma bebida, acumula responsabilidades de várias naturezas: gestão de pedido (`createOrder`, `addToOrder`, `confirmOrder`), dados cadastrais do cliente (nome, endereço, telefone, e-mail), notificações/promoções, programa de fidelidade, tratamento de reclamações e atendimento ao cliente. Essa concentração excessiva de responsabilidades e de atributos não coesos é característica de uma God Class.

---

## 2. Lazy Class (Classe Preguiçosa)

**Onde:** Classe `Drink` e seus métodos vazios `anotherUnusedMethod()` e `yetAnotherUnusedMethod()`.

**Trecho:**
```java
public void anotherUnusedMethod() {
}

public void yetAnotherUnusedMethod() {
}
```

**Justificativa:** Há métodos que não executam nenhuma ação e não agregam valor à classe, indicando elementos "preguiçosos" que não justificam sua existência. A presença de atributos como `tempDiscountCode` e `tempOrderNote`, declarados mas nunca utilizados, também reforça essa característica.

---

## 3. Long Method (Método Longo)

**Onde:** Método `longMethod()`.

**Trecho:**
```java
public void longMethod() {
    System.out.println("Drink is handling many tasks in a single method");
    this.createOrder("Cola");
    this.addToOrder();
    this.confirmOrder();
    this.updateCustomerInfo("Jane", "Doe", "456 Avenue", "555-6666", "jane.doe@example.com");
    this.notifyForPromotion();
    this.notifyForDiscount();
    this.notifyForNewArrivals();
    this.applyDiscount();
    this.applyLoyaltyPoints();
    this.handleComplaint("cold drink");
}
```

**Justificativa:** O método executa uma sequência extensa de tarefas distintas em um único bloco, misturando criação de pedido, atualização de dados, notificações, descontos e reclamações. A quantidade de operações e responsabilidades acumuladas torna o método longo e difícil de manter.

---

## 4. Duplicated Code (Código Duplicado)

**Onde:** Método `duplicateMethod()`.

**Trecho:**
```java
public void duplicateMethod() {
    this.createOrder("Cola");
    this.createOrder("Cola");
}
```

**Justificativa:** Há chamadas idênticas e repetidas (`createOrder("Cola")`) dentro do mesmo método, caracterizando duplicação de código.

---

## 5. Divergent Change / Shotgun Surgery (relacionado a mudanças)

**Onde:** Métodos `updateCustomerInfo`, `updateCustomerName`, `updateCustomerAddress`, `updateCustomerPhoneNumber`, `updateCustomerEmail`.

**Trecho:**
```java
public void updateCustomerInfo(String firstName, String lastName, String address, String phoneNumber, String email) { ... }
public void updateCustomerName(String firstName, String lastName) { ... }
public void updateCustomerAddress(String address) { ... }
public void updateCustomerPhoneNumber(String phoneNumber) { ... }
public void updateCustomerEmail(String email) { ... }
```

**Justificativa:** A lógica de atualização dos dados do cliente está espalhada por vários métodos que escrevem nos mesmos atributos, de modo que uma alteração na forma de tratar os dados do cliente exigiria modificar múltiplos pontos. Esse espalhamento de uma mesma responsabilidade por diversos métodos caracteriza sintomas como Divergent Change / Shotgun Surgery.

---

## 6. Middle Man (Homem do Meio)

**Onde:** Métodos `middlemanMethod()` e `middleMethod()`.

**Trecho:**
```java
public void middlemanMethod() {
    System.out.println("Drink is calling a middleman method");
    this.middleMethod();
}

public void middleMethod() {
    System.out.println("Middleman method delegating to another method");
    this.realMethod();
}
```

**Justificativa:** Esses métodos apenas delegam a chamada para outros métodos, sem adicionar comportamento relevante. `middleMethod()` repassa a execução para `realMethod()`, e `middlemanMethod()` repassa para `middleMethod()`, configurando uma cadeia de intermediários.

---

## 7. Message Chains (Cadeia de Mensagens) / Chain of Methods

**Onde:** Método `chainOfMethods()`.

**Trecho:**
```java
public void chainOfMethods() {
    System.out.println("Drink is initiating a message chain");
    this.updateCustomerAddress("456 Avenue");
}
```

**Justificativa:** O nome e a estrutura do método indicam um encadeamento de chamadas (mensagens) disparado pela classe, em que uma operação presume navegação/sequência de acessos entre objetos, típico de Message Chain em que o cliente é fortemente acoplado à estrutura interna de colaboradores.

---

## 8. Feature Envy (Inveja de Funcionalidade)

**Onde:** Métodos `notifyForPromotion`, `notifyForDiscount`, `notifyForNewArrivals`, `applyDiscount`, `applyLoyaltyPoints`, `handleComplaint`, `askForReceipt` (comportamentos ligados ao cliente).

**Trecho:**
```java
public void notifyForPromotion() { System.out.println("Notifying customer for promotion"); }
public void notifyForDiscount() { System.out.println("Notifying customer for discount"); }
public void applyDiscount() { System.out.println("Applying discount for customer"); }
public void applyLoyaltyPoints() { System.out.println("Applying loyalty points for customer"); }
public void handleComplaint(String complaint) { ... }
public void askForReceipt() { System.out.println("Customer is asking for a receipt."); }
```

**Justificativa:** Métodos que tratam explicitamente de notificações, promoções, fidelidade, reclamações e atendimento referem-se a responsabilidades do cliente, e não da bebida. Essa apropriação de comportamento pertencente a outra abstração (o cliente) configura Feature Envy.

---

## 9. Inappropriate Intimacy (Intimidade Inapropriada)

**Onde:** Método `accessInternalDetails()`.

**Trecho:**
```java
public void accessInternalDetails() {
    System.out.println("Accessing internal details: " + this.drinkType);
}
```

**Justificativa:** O método expõe/depende diretamente do detalhe interno `drinkType`, realizando acesso a informação que deveria ser encapsulada, configurando um caso de intimidade inapropriada com os próprios detalhes internos.

---

## 10. Refused Bequest (Herança Recusada) — sintoma de classe base inadequada

**Onde:** Método `refusedBequest()`.

**Trecho:**
```java
public void refusedBequest() {
}
```

**Justificativa:** A presença de um método explicitamente vazio chamado `refusedBequest` representa o sintoma de uma subclasse que herda comportamento/membros que não utiliza ou rejeita — a herança recusada. O método vazio evidencia que o elemento herdado (ou previsto) não é aproveitado pela classe.

---

## 11. Dead Code (Código Morto)

**Onde:** Métodos `anotherUnusedMethod()` e `yetAnotherUnusedMethod()`; atributos `tempDiscountCode` e `tempOrderNote`.

**Trecho:**
```java
private String tempDiscountCode;
private String tempOrderNote;
...
public void anotherUnusedMethod() { }
public void yetAnotherUnusedMethod() { }
```

**Justificativa:** Há membros declarados que nunca são utilizados em nenhum ponto do código — métodos vazios e nunca invocados, além de atributos `temp*` nunca lidos nem escritos. Esses elementos configuram código morto.

---

## 12. Comments/Variáveis com nomes temporárias e não significativas (sugestivo de smell)

**Onde:** Atributos `tempDiscountCode`, `tempOrderNote`.

**Trecho:**
```java
private String tempDiscountCode;
private String tempOrderNote;
```

**Justificativa:** O prefixo "temp" e o fato de serem atributos não utilizados indicam declarações provisórias/esquecidas, um sintoma de má organização da classe que se conecta ao Dead Code e à Lazy Class.

---

## 13. Switch/If-Else condicional complexa (Conditional Complexity)

**Onde:** Método `handleComplaint(String complaint)`.

**Trecho:**
```java
public void handleComplaint(String complaint) {
    if (complaint.equals("cold drink")) {
        System.out.println("Handling complaint: Drink is cold");
    } else if (complaint.equals("wrong drink")) {
        System.out.println("Handling complaint: Wrong drink delivered");
    } else {
        System.out.println("Handling complaint: General complaint");
    }
}
```

**Justificativa:** A lógica de tratamento de reclamações é implementada por meio de encadeamento de condicionais `if/else if`, concentrando a decisão sobre múltiplos tipos de caso dentro da classe `Drink`. Essa estrutura condicional extensa é um code smell típico, especialmente quando a lógica pertence a outra abstração.

---

## 14. Temporary Field (Campo Temporário)

**Onde:** Atributos `tempDiscountCode` e `tempOrderNote`.

**Trecho:**
```java
private String tempDiscountCode;
private String tempOrderNote;
```

**Justificativa:** Esses atributos têm nomes que remetem a valores temporários e não participam de nenhum fluxo real da classe. Declarar campos que só seriam usados em situações específicas (ou que nunca são usados) é o sintoma de Temporary Field, contribuindo para a baixa coesão da classe.

---

### Resumo dos smells identificados

| # | Code Smell | Onde |
|---|-----------|------|
| 1 | God Class / Blob | Classe `Drink` |
| 2 | Lazy Class | Classe `Drink`, métodos vazios |
| 3 | Long Method | `longMethod()` |
| 4 | Duplicated Code | `duplicateMethod()` |
| 5 | Divergent Change / Shotgun Surgery | métodos `updateCustomer*` |
| 6 | Middle Man | `middlemanMethod()`, `middleMethod()` |
| 7 | Message Chains | `chainOfMethods()` |
| 8 | Feature Envy | `notify*`, `apply*`, `handleComplaint`, `askForReceipt` |
| 9 | Inappropriate Intimacy | `accessInternalDetails()` |
| 10 | Refused Bequest | `refusedBequest()` |
| 11 | Dead Code | `anotherUnusedMethod()`, `yetAnotherUnusedMethod()`, `tempDiscountCode`, `tempOrderNote` |
| 12/14 | Temporary Field / Variáveis mal nomeadas | `tempDiscountCode`, `tempOrderNote` |
| 13 | Condicional complexa (Switch Statements) | `handleComplaint()` |

Observação: trata-se de um código-fonte propositalmente construído para conter code smells (dataset para fins de pesquisa/refatoração), conforme indicado no próprio comentário de licença no topo do arquivo.