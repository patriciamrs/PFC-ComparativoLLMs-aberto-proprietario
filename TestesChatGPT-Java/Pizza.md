
# Análise de Code Smells – Classe Pizza

### 1. Large Class (Classe Grande)

**Localização:** Classe `Pizza`.

**Justificativa:** A classe concentra diversas responsabilidades, incluindo configuração da pizza, gerenciamento de informações de clientes, notificações, descontos, reclamações e pedidos. Essa quantidade de responsabilidades distintas caracteriza uma classe excessivamente abrangente.

### 2. Long Method (Método Longo)

**Localização:** Método `longMethod()`.

**Justificativa:** O método reúne diversas operações relacionadas à configuração da pizza, atualização de dados do cliente, notificações, descontos e tratamento de reclamações. A concentração de diferentes tarefas em um único método caracteriza esse code smell.

### 3. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Métodos `updateCustomerInfo()` e `orderWithUnnecessaryDetails()`.

**Justificativa:** O método `updateCustomerInfo()` recebe cinco parâmetros relacionados às informações do cliente, enquanto `orderWithUnnecessaryDetails()` recebe seis parâmetros relacionados ao pedido. Essas listas extensas aumentam a complexidade das chamadas e dificultam a compreensão dos métodos.

### 4. Data Clumps (Agrupamentos de Dados)

**Localização:** Atributos `customerFirstName`, `customerLastName`, `customerAddress`, `customerPhoneNumber` e `customerEmail`, além dos parâmetros correspondentes do método `updateCustomerInfo()`.

**Justificativa:** Os atributos representam um conjunto de informações relacionadas ao mesmo conceito, os dados cadastrais do cliente. Esses dados aparecem agrupados na classe e na assinatura do método, caracterizando um agrupamento de dados.

### 5. Primitive Obsession (Obsessão por Tipos Primitivos)

**Localização:** Atributos `size`, `doughType`, `topping` e `extraCheese`, além dos parâmetros utilizados para representar características da pizza.

**Justificativa:** O código utiliza tipos simples, como `String` e `boolean`, para representar características específicas do domínio, como tamanho, tipo de massa, cobertura e queijo extra. Essas informações são manipuladas diretamente por meio de tipos básicos, sem uma representação própria das regras e dos conceitos envolvidos.

### 6. Temporary Field (Campo Temporário)

**Localização:** Atributos `tempDiscountCode` e `tempOrderNote`.

**Justificativa:** Os atributos são declarados na classe `Pizza`, mas não são inicializados explicitamente nem utilizados pelos métodos apresentados. Sua presença sugere campos destinados a situações específicas, sem participação no comportamento habitual da classe. Entretanto, não é possível confirmar pelo código que sejam utilizados temporariamente.

### 7. Duplicate Code (Código Duplicado)

**Localização:** Método `duplicateMethod()`.

**Trecho:**
```java
this.setTopping("Cheese");
this.setTopping("Cheese");
```

**Justificativa:** O método executa duas vezes consecutivas a mesma chamada, com o mesmo argumento, produzindo uma repetição desnecessária da operação.

### 8. Switch Statements / Repeated Switches (Condicionais por Tipo)

**Localização:** Método `handleComplaint(String complaint)`.

**Justificativa:** O método apresenta uma sequência de condições `if/else if` que verifica diferentes valores textuais de reclamações, como `"cold pizza"`, `"late delivery"` e `"wrong order"`, para determinar o comportamento executado. Essa estrutura apresenta uma seleção baseada em valores específicos. Entretanto, uma única cadeia condicional não é suficiente para confirmar o code smell `Repeated Switches` da segunda edição de Fowler.

### 9. Middle Man (Intermediário)

**Localização:** Método `middleMethod()`.

**Trecho:**
```java
public void middleMethod() {
    System.out.println("Middleman method delegating to another method");
    this.realMethod();
}
```

**Justificativa:** O método atua principalmente como intermediário para a execução de `realMethod()`, acrescentando apenas uma mensagem ao console. Essa delegação apresenta um nível de intermediação com pouca responsabilidade própria, embora não demonstre que a classe inteira funcione predominantemente como intermediária.

### 10. Dead Code (Código Morto)

**Localização:** Métodos `anotherUnusedMethod()`, `yetAnotherUnusedMethod()` e `refusedBequest()`.

**Trecho:**
```java
public void anotherUnusedMethod() {
}

public void yetAnotherUnusedMethod() {
}

public void refusedBequest() {
}
```

**Justificativa:** Os três métodos possuem implementações vazias e não são chamados em nenhum trecho apresentado. Não desempenham nenhuma operação e representam código sem funcionalidade observável no contexto analisado.

### 11. Lazy Class (Classe Preguiçosa)

**Localização:** Classes `VeggiePizza`, `TunaPizza` e `PepperoniPizza`.

**Justificativa:** Essas subclasses possuem apenas construtores que definem valores específicos para a classe `Pizza`, sem implementar comportamentos adicionais. Sua contribuição limitada pode caracterizar o code smell Lazy Class, embora a existência de tipos distintos de pizza também possa justificar essas subclasses dependendo do restante do sistema.

---

## Resumo dos Code Smells Identificados

| Code Smell | Localização |
|---|---|
| Large Class | `Pizza` |
| Long Method | `longMethod()` |
| Long Parameter List | `updateCustomerInfo()`, `orderWithUnnecessaryDetails()` |
| Data Clumps | Dados do cliente e `updateCustomerInfo()` |
| Primitive Obsession | Atributos e parâmetros das características da pizza |
| Temporary Field | `tempDiscountCode`, `tempOrderNote` |
| Duplicate Code | `duplicateMethod()` |
| Switch Statements | `handleComplaint()` |
| Middle Man | `middleMethod()` |
| Dead Code | Três métodos vazios |
| Lazy Class | `VeggiePizza`, `TunaPizza`, `PepperoniPizza` |

**Observação:** Os casos de Temporary Field, Middle Man, Lazy Class e Repeated Switches possuem limitações de evidência, conforme indicado nas justificativas. Portanto, não devem ser tratados como ocorrências definitivamente comprovadas apenas pelo código fornecido. Também não há evidências suficientes para classificar `chainOfMethods()` como Message Chains, `accessInternalDetails()` como Inappropriate Intimacy ou a herança apresentada como Refused Bequest.
