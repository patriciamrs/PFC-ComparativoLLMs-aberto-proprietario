
# Análise de Code Smells – Classe `Cashier`

A análise foi realizada considerando os *code smells* descritos por Martin Fowler no livro *Refatoração: Aperfeiçoando o Design de Códigos Existentes*, com base nas evidências presentes no código fornecido.

### 1. Data Clumps (Agrupamento de Dados)

**Localização:** Atributos `firstName`, `lastName`, `address`, `phoneNumber` e `email`, além do método `updateContactInfo()`.

**Justificativa:** Os atributos representam um conjunto de informações relacionadas ao contato de uma pessoa e aparecem agrupados como parâmetros no método `updateContactInfo()`. Essa associação caracteriza um agrupamento de dados que poderia representar um conceito próprio.

### 2. Temporary Field (Campo Temporário)

**Localização:** Atributos `tempDiscountCode` e `tempOrderNote`.

**Justificativa:** Os atributos são declarados na classe, mas não são inicializados explicitamente nem utilizados nos métodos apresentados. Isso sugere a existência de campos destinados a situações específicas, embora o uso temporário não possa ser confirmado apenas pelo código.

### 3. Duplicate Code (Código Duplicado)

**Localização:** Método `handleComplaint()`.

```java
if (complaint.equals("cold pizza")) {
    this.calmCustomerDown();
} else if (complaint.equals("late delivery")) {
    this.calmCustomerDown();
} else if (complaint.equals("wrong order")) {
    this.calmCustomerDown();
} else {
    this.calmCustomerDown();
}
```

**Justificativa:** Todas as condições executam exatamente a mesma chamada ao método `calmCustomerDown()`, apresentando repetição de comportamento em diferentes ramificações.

**Localização adicional:** Método `duplicateMethod()`.

```java
this.takeOrder("Cheese");
this.takeOrder("Cheese");
```

**Justificativa:** A mesma chamada é executada duas vezes consecutivas com o mesmo argumento. Embora possa ser intencional, constitui uma repetição literal de instruções.

### 4. Middle Man (Intermediário)

**Localização:** Métodos `middlemanMethod()` e `middleMethod()`.

```java
public void middlemanMethod() {
    System.out.println("Cashier is calling a middleman method");
    this.middleMethod();
}

public void middleMethod() {
    System.out.println("Middleman method delegating to another method");
    this.realMethod();
}
```

**Justificativa:** Os métodos introduzem níveis intermediários de chamadas até `realMethod()`, sem acrescentar lógica significativa além das mensagens exibidas. Isso caracteriza uma estrutura de delegação desnecessariamente indireta.

### 5. Large Class (Classe Grande)

**Localização:** Classe `Cashier`.

**Justificativa:** A classe reúne diversas responsabilidades, incluindo atendimento de pedidos, comunicação com o cozinheiro, gerenciamento de informações de contato, notificações promocionais, aplicação de benefícios e tratamento de reclamações. Essa diversidade indica concentração de responsabilidades pouco relacionadas em uma única classe.

### 6. Switch Statements (Estruturas Condicionais Repetitivas)

**Localização:** Método `handleComplaint()`.

```java
if (complaint.equals("cold pizza")) {
    this.calmCustomerDown();
} else if (complaint.equals("late delivery")) {
    this.calmCustomerDown();
} else if (complaint.equals("wrong order")) {
    this.calmCustomerDown();
} else {
    this.calmCustomerDown();
}
```

**Justificativa:** O método apresenta uma sequência de verificações condicionais baseada em valores literais de uma string. Entretanto, como todos os caminhos executam a mesma operação, o problema mais evidente nesse trecho é a duplicação de código, e não a existência de comportamentos condicionais distintos.

### 7. Feature Envy (Inveja de Funcionalidade)

**Localização:** Método `accessInternalDetails()`.

```java
public void accessInternalDetails() {
    System.out.println("Accessing internal details of Chef: " + chef.isBusy());
}
```

**Justificativa:** O método consulta o estado de um objeto de outra classe (`Chef`). Entretanto, uma única consulta não é suficiente para caracterizar *Feature Envy* de forma conclusiva, pois esse *code smell* normalmente envolve métodos que utilizam mais intensamente os dados de outra classe do que os da própria classe.

---

## Resumo da análise

| Code Smell | Localização | Avaliação |
|---|---|---|
| Data Clumps | Atributos de contato e `updateContactInfo()` | Identificado |
| Temporary Field | `tempDiscountCode`, `tempOrderNote` | Possível, não confirmado |
| Duplicate Code | `handleComplaint()` | Identificado |
| Duplicate Code | `duplicateMethod()` | Repetição literal, não conclusiva |
| Middle Man | `middlemanMethod()`, `middleMethod()` | Identificado |
| Large Class | Classe `Cashier` | Identificado |
| Switch Statements | `handleComplaint()` | Indício, não conclusivo |
| Feature Envy | `accessInternalDetails()` | Não confirmado |

**Observação:** Os métodos `longMethod()`, `chainOfMethods()` e `refusedBequest()` possuem nomes sugestivos, mas não apresentam, respectivamente, evidências suficientes de *Long Method*, *Message Chains* ou *Refused Bequest*. Da mesma forma, a utilização de `boolean` em `frequentCustomerDiscount` não caracteriza, isoladamente, *Primitive Obsession*, e o método vazio `anotherUnusedMethod()` não comprova a existência de *Dead Code*, pois ele pode ser chamado externamente.

Assim, para uma análise restrita aos *code smells* sustentados pelo código apresentado, as ocorrências mais evidentes são **Data Clumps, Duplicate Code, Middle Man e Large Class**.
