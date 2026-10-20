
# Análise de Code Smells — Classe `Customer`

### 1. Data Clumps (Agrupamento de Dados)

**Localização:** Atributos `firstName`, `lastName`, `address`, `phoneNumber` e `email`, além do método `updateContactInfo()`.

**Trecho:**
```java
private String firstName;
private String lastName;
private String address;
private String phoneNumber;
private String email;
```

**Justificativa:** Os atributos representam um conjunto de informações relacionadas ao contato do cliente. Esses mesmos dados aparecem agrupados como parâmetros no método `updateContactInfo()`, indicando um agrupamento de dados utilizados em conjunto.

### 2. Temporary Field (Campo Temporário)

**Localização:** Atributos `tempDiscountCode` e `tempOrderNote`.

**Trecho:**
```java
private String tempDiscountCode;
private String tempOrderNote;
```

**Justificativa:** Os atributos foram declarados na classe, mas não são utilizados nos métodos apresentados. Seus nomes sugerem que seriam necessários apenas em determinadas situações, embora seu uso temporário não possa ser confirmado pelo código.

### 3. Dead Code (Código Morto)

**Localização:** Métodos `anotherUnusedMethod()` e `refusedBequest()`, além dos atributos `tempDiscountCode`, `tempOrderNote` e `frequentCustomerDiscount`.

**Trecho:**
```java
public void anotherUnusedMethod() {
}

public void refusedBequest() {
}
```

**Justificativa:** Os métodos possuem corpos vazios e não apresentam comportamento implementado. Além disso, os atributos mencionados não são utilizados de maneira funcional no código apresentado, caracterizando elementos sem contribuição efetiva para o comportamento da classe.

### 4. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Método `orderWithUnnecessaryDetails()`.

**Trecho:**
```java
public void orderWithUnnecessaryDetails(
    String pizzaType,
    String size,
    String crustType,
    String toppings,
    boolean extraCheese,
    String discountCode
)
```

**Justificativa:** O método recebe seis parâmetros diferentes para representar os detalhes de um pedido. A quantidade de argumentos aumenta a complexidade de sua utilização. Além disso, apenas `pizzaType` é utilizado na chamada que efetivamente encaminha o pedido.

### 5. Message Chains (Cadeias de Mensagens)

**Localização:** Métodos `chainOfMethods()`, `complain()` e `accessInternalDetails()`.

**Trechos:**
```java
this.pizzaShop.getCashier().getChef().cleanKitchen();

this.pizzaShop.getCashier().calmCustomerDown();

pizzaShop.getCashier().getChef().isBusy();
```

**Justificativa:** Os métodos acessam objetos intermediários por meio de chamadas encadeadas para alcançar funcionalidades de outros objetos. Isso faz com que a classe `Customer` conheça detalhes da estrutura interna de suas dependências, aumentando o acoplamento.

### 6. Middle Man (Intermediário)

**Localização:** Método `middleMethod()`.

**Trecho:**
```java
public void middleMethod() {
    System.out.println("Middleman method delegating to another method");
    this.realMethod();
}
```

**Justificativa:** O método atua principalmente como intermediário entre `middlemanMethod()` e `realMethod()`, encaminhando a execução para outro método sem acrescentar uma operação significativa além da mensagem exibida.

### 7. Duplicated Code (Código Duplicado)

**Localização:** Método `duplicateComplaint()`.

**Trecho:**
```java
this.complain("Pizza is cold");
this.complain("Pizza is cold");
this.complain("Pizza is late");
this.complain("Pizza is late");
```

**Justificativa:** O método apresenta chamadas idênticas repetidas consecutivamente, executando as mesmas operações com os mesmos argumentos. Essa repetição caracteriza duplicação de instruções no código.

### 8. Large Class (Classe Grande)

**Localização:** Classe `Customer`.

**Justificativa:** A classe reúne diversas responsabilidades, incluindo realização de pedidos, reclamações, atualização de informações pessoais, notificações promocionais, aplicação de descontos e gerenciamento de pontos de fidelidade. A concentração dessas funcionalidades indica que a classe acumula diferentes responsabilidades, caracterizando uma classe com escopo excessivamente amplo.

### 9. Feature Envy (Inveja de Funcionalidade)

**Localização:** Métodos `chainOfMethods()` e `accessInternalDetails()`.

**Trechos:**
```java
this.pizzaShop.getCashier().getChef().cleanKitchen();

pizzaShop.getCashier().getChef().isBusy();
```

**Justificativa:** Os métodos dependem de funcionalidades e informações pertencentes a outros objetos, especialmente `Chef`. A classe `Customer` acessa essas funcionalidades por meio de objetos intermediários, demonstrando interesse em comportamentos que não pertencem diretamente à sua responsabilidade.

### 10. Divergent Change (Mudança Divergente)

**Localização:** Classe `Customer`.

**Justificativa:** A classe concentra funcionalidades relacionadas a diferentes áreas do sistema, como pedidos, informações cadastrais, promoções, descontos e reclamações. Dessa forma, alterações em diferentes regras de negócio podem exigir modificações na mesma classe por motivos distintos, indicando múltiplas razões potenciais para mudanças.

---

## Resumo dos Code Smells Identificados

| Code Smell | Localização |
|---|---|
| Data Clumps | Atributos de contato e `updateContactInfo()` |
| Temporary Field | `tempDiscountCode`, `tempOrderNote` |
| Dead Code | Métodos vazios e atributos sem uso funcional |
| Long Parameter List | `orderWithUnnecessaryDetails()` |
| Message Chains | `chainOfMethods()`, `complain()`, `accessInternalDetails()` |
| Middle Man | `middleMethod()` |
| Duplicated Code | `duplicateComplaint()` |
| Large Class | Classe `Customer` |
| Feature Envy | `chainOfMethods()`, `accessInternalDetails()` |
| Divergent Change | Classe `Customer` |

**Observação:** A identificação de `Large Class`, `Feature Envy` e `Divergent Change` envolve interpretação das responsabilidades da classe. Já `Dead Code` e `Temporary Field` foram avaliados com base apenas no código apresentado, pois não é possível verificar eventuais utilizações externas dos membros públicos ou confirmar se os campos temporários são usados em outras partes da implementação. Não foram considerados `Primitive Obsession` apenas pela existência de atributos primitivos, `Long Method` apenas pelo número de linhas, nem `Refused Bequest` apenas pelo nome de um método.
