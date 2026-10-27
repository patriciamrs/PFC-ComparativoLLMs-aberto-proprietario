
# Análise de Code Smells — Classe Shop (Java)

### 1. Large Class (Classe Grande)

- **Localização:** Classe `Shop`.
- **Justificativa:** A classe concentra diversas responsabilidades, incluindo gerenciamento de pedidos, criação de pizzas, armazenamento de informações de contato, notificações promocionais, aplicação de descontos e tratamento de reclamações. Essa quantidade de responsabilidades caracteriza uma classe com funcionalidades pouco relacionadas entre si.

### 2. Long Parameter List (Lista Longa de Parâmetros)

- **Localização:** Método `updateContactInfo()`.
- **Trecho:**

```java
public void updateContactInfo(String firstName, String lastName, String address, String phoneNumber, String email)
```

- **Justificativa:** O método recebe cinco parâmetros relacionados às informações de contato. A quantidade de parâmetros aumenta a complexidade da chamada e dificulta a compreensão e manutenção do código.

### 3. Data Clumps (Agrupamentos de Dados)

- **Localização:** Atributos `firstName`, `lastName`, `address`, `phoneNumber` e `email`, presentes na classe `Shop` e utilizados no método `updateContactInfo()`.
- **Trecho:**

```java
private String firstName;
private String lastName;
private String address;
private String phoneNumber;
private String email;
```

- **Justificativa:** Os atributos representam informações relacionadas a uma mesma entidade e aparecem agrupados na declaração da classe e nos parâmetros do método `updateContactInfo()`, caracterizando um conjunto de dados utilizados em conjunto.

### 4. Primitive Obsession (Obsessão por Tipos Primitivos)

- **Localização:** Atributos de contato e método `createPizza()`.
- **Trecho:**

```java
private String address;
private String phoneNumber;
private String email;
private String tempDiscountCode;
```

```java
public Pizza createPizza(String pizzaType)
```

- **Justificativa:** O código utiliza repetidamente valores do tipo `String` para representar informações de domínio, como endereço, telefone, e-mail, códigos de desconto e tipos de pizza. Esses conceitos são tratados diretamente como textos, sem uma representação específica de suas características.

### 5. Switch Statements (Estruturas Condicionais Repetitivas)

- **Localização:** Método `createPizza()`.
- **Trecho:**

```java
if (pizzaType.equals("Cheese")) {
    return new CheesePizza();
} else if (pizzaType.equals("Veggie")) {
    return new VeggiePizza();
} else if (pizzaType.equals("Tuna")) {
    return new TunaPizza();
} else if (pizzaType.equals("Pepperoni")) {
    return new PepperoniPizza();
} else {
    throw new IllegalArgumentException("Unknown pizza type");
}
```

- **Justificativa:** O método utiliza uma sequência de condicionais para determinar qual classe de pizza deve ser instanciada com base em um valor textual. Essa estrutura concentra a seleção de diferentes tipos de objetos em uma cadeia de verificações condicionais.

### 6. Duplicated Code (Código Duplicado)

- **Localização:** Método `handleComplaint()`.
- **Trecho:**

```java
if (complaint.equals("cold pizza")) {
    cashier.calmCustomerDown();
} else if (complaint.equals("late delivery")) {
    cashier.calmCustomerDown();
} else if (complaint.equals("wrong order")) {
    cashier.calmCustomerDown();
} else {
    cashier.calmCustomerDown();
}
```

- **Justificativa:** Todas as condições executam exatamente a mesma instrução, `cashier.calmCustomerDown()`, independentemente do tipo de reclamação. Isso caracteriza duplicação de código dentro do mesmo método.

### 7. Dead Code (Código Morto)

- **Localização:** Método `anotherUnusedMethod()`.
- **Trecho:**

```java
public void anotherUnusedMethod() {
}
```

- **Justificativa:** O método possui implementação vazia e não realiza nenhuma operação. Além disso, não há referências à sua utilização no código apresentado, indicando a presença de código sem funcionalidade aparente.

### 8. Temporary Field (Campo Temporário)

- **Localização:** Atributos `tempDiscountCode` e `tempOrderNote`.
- **Trecho:**

```java
private String tempDiscountCode;
private String tempOrderNote;
```

- **Justificativa:** Os atributos representam informações temporárias e não são inicializados nem utilizados pelos métodos apresentados. Sua presença sugere campos associados a situações específicas, sem participação no comportamento normal da classe.

### 9. Divergent Change (Mudança Divergente)

- **Localização:** Classe `Shop`.
- **Justificativa:** A classe reúne funcionalidades de diferentes áreas, como criação de pizzas (`createPizza()`), gerenciamento de pedidos (`receiveOrder()`), informações de contato (`updateContactInfo()`), promoções (`notifyForPromotion()`) e reclamações (`handleComplaint()`). Dessa forma, alterações em responsabilidades distintas podem exigir modificações na mesma classe.
