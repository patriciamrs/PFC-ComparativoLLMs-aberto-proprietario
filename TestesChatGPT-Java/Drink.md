
# Análise de Code Smells – Classe Drink (Java)

### 1. Large Class (Classe Grande)

**Localização:** Classe `Drink`.

**Justificativa:** A classe possui diversos atributos e métodos que representam diferentes responsabilidades, incluindo gerenciamento de bebidas, informações de clientes, notificações promocionais, descontos e reclamações. Essa concentração de responsabilidades caracteriza uma classe excessivamente abrangente.

### 2. Long Method (Método Longo)

**Localização:** Método `longMethod()`.

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

**Justificativa:** O método reúne diversas operações relacionadas a pedidos, atualização de clientes, notificações, descontos e reclamações. Embora não seja muito extenso em número de linhas, concentra tarefas distintas em uma única operação.

### 3. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Método `updateCustomerInfo()`.

```java
public void updateCustomerInfo(String firstName, String lastName, String address, String phoneNumber, String email)
```

**Justificativa:** O método recebe cinco parâmetros relacionados às informações pessoais do cliente, caracterizando uma lista extensa de argumentos.

### 4. Data Clumps (Agrupamento de Dados)

**Localização:** Atributos da classe `Drink` e método `updateCustomerInfo()`.

```java
private String customerFirstName;
private String customerLastName;
private String customerAddress;
private String customerPhoneNumber;
private String customerEmail;
```

**Justificativa:** Os atributos representam informações relacionadas a uma mesma entidade, o cliente, e aparecem agrupados tanto na declaração da classe quanto nos parâmetros do método `updateCustomerInfo()`. Isso evidencia um conjunto de dados relacionados que são manipulados em conjunto.

### 5. Divergent Change (Mudança Divergente)

**Localização:** Classe `Drink`.

**Justificativa:** A classe reúne responsabilidades relacionadas ao gerenciamento de bebidas, cadastro de clientes, promoções, descontos e reclamações. Dessa forma, alterações em diferentes funcionalidades do sistema podem exigir modificações na mesma classe por motivos distintos.

### 6. Temporary Field (Campo Temporário)

**Localização:** Atributos `tempDiscountCode` e `tempOrderNote`.

```java
private String tempDiscountCode;
private String tempOrderNote;
```

**Justificativa:** Os atributos indicam dados temporários e não são utilizados pelos métodos apresentados. Sua presença sugere campos que não fazem parte do estado regularmente utilizado pela classe. Entretanto, sem evidência de uso apenas em determinadas circunstâncias, a classificação como *Temporary Field* é apenas indicativa.

### 7. Dead Code (Código Morto)

**Localização:** Métodos `anotherUnusedMethod()`, `yetAnotherUnusedMethod()` e `refusedBequest()`.

```java
public void anotherUnusedMethod() {
}

public void yetAnotherUnusedMethod() {
}

public void refusedBequest() {
}
```

**Justificativa:** Os três métodos possuem corpos vazios e não apresentam qualquer comportamento implementado. Além disso, não são chamados em nenhum trecho da classe apresentada.

### 8. Duplicate Code (Código Duplicado)

**Localização:** Método `duplicateMethod()`.

```java
public void duplicateMethod() {
    this.createOrder("Cola");
    this.createOrder("Cola");
}
```

**Justificativa:** O método contém duas chamadas consecutivas e idênticas, repetindo a mesma operação com o mesmo argumento.

### 9. Middle Man (Intermediário)

**Localização:** Método `middleMethod()`.

```java
public void middleMethod() {
    System.out.println("Middleman method delegating to another method");
    this.realMethod();
}
```

**Justificativa:** O método atua principalmente como intermediário, encaminhando a execução para `realMethod()`, sem acrescentar uma lógica de negócio significativa. Entretanto, a ocorrência é limitada a um método e não demonstra que a classe inteira seja excessivamente delegadora.

### 10. Speculative Generality (Generalidade Especulativa)

**Localização:** Métodos `anotherUnusedMethod()`, `yetAnotherUnusedMethod()` e `refusedBequest()`.

**Justificativa:** Esses métodos estão declarados, mas não possuem implementação nem utilização demonstrada no código. Podem representar estruturas adicionadas para possíveis necessidades futuras, sem funcionalidade atual identificável.

---

## Observações sobre a classificação

Alguns pontos exigem cuidado para evitar falsos positivos:

- **Message Chains:** O método `chainOfMethods()` realiza apenas uma chamada a outro método da própria classe. Portanto, não caracteriza uma cadeia de mensagens.
- **Feature Envy:** O método `accessInternalDetails()` acessa um atributo da própria classe, não dados de outra classe. Portanto, não caracteriza esse smell.
- **Refused Bequest:** Apesar da existência de um método chamado `refusedBequest()`, não há herança no código apresentado. Portanto, esse smell não pode ser confirmado.
- **Middle Man:** A delegação isolada de `middleMethod()` constitui, no máximo, um indício fraco desse smell.
- **Dead Code:** Os métodos vazios não possuem comportamento, mas a ausência de chamadas dentro da classe não comprova que métodos públicos nunca sejam utilizados externamente.
- **Speculative Generality e Temporary Field:** São classificações possíveis, mas dependem de informações adicionais sobre a finalidade dos elementos.

**Conclusão:** As ocorrências mais claramente sustentadas pelo código são *Large Class*, *Long Parameter List*, *Data Clumps*, *Divergent Change* e a concentração de responsabilidades em `longMethod()`. Os demais itens apresentam indícios, mas devem ser avaliados com cautela antes de serem considerados ocorrências confirmadas no conjunto de referência.
