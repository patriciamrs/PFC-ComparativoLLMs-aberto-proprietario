# Análise de Code Smells — Classe Drink

### 1. Data Clumps (Agrupamento de Dados)

**Localização:** Classe `Drink`, atributos relacionados às informações do cliente e método `updateCustomerInfo()`.

**Trecho:**
    private String customerFirstName;
    private String customerLastName;
    private String customerAddress;
    private String customerPhoneNumber;
    private String customerEmail;

**Justificativa:** Os atributos representam um conjunto de informações relacionadas ao cliente, que também aparecem agrupadas como parâmetros no método `updateCustomerInfo()`. Essa associação caracteriza um agrupamento de dados que poderia constituir uma estrutura própria.

### 2. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Método `updateCustomerInfo()`.

**Trecho:**
    public void updateCustomerInfo(String firstName, String lastName,
        String address, String phoneNumber, String email)

**Justificativa:** O método recebe cinco parâmetros individuais relacionados às informações de um mesmo cliente, caracterizando uma lista extensa de parâmetros.

### 3. Temporary Field (Campo Temporário)

**Localização:** Classe `Drink`, atributos `tempDiscountCode` e `tempOrderNote`.

**Trecho:**
    private String tempDiscountCode;
    private String tempOrderNote;

**Justificativa:** Os atributos são declarados, mas não são inicializados explicitamente nem utilizados nos métodos apresentados. Sua presença sugere campos destinados a situações específicas, embora o uso temporário não possa ser confirmado apenas pelo código.

### 4. Large Class (Classe Grande)

**Localização:** Classe `Drink`.

**Justificativa:** A classe concentra diversas responsabilidades, incluindo criação e confirmação de pedidos, atualização de informações de clientes, envio de notificações, aplicação de descontos, gerenciamento de pontos de fidelidade e tratamento de reclamações. Essa concentração de funcionalidades caracteriza uma classe com responsabilidades excessivas.

### 5. Long Method (Método Longo)

**Localização:** Método `longMethod()`.

**Trecho:**
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

**Justificativa:** O método reúne diversas operações de responsabilidades distintas, como criação de pedidos, atualização de clientes, notificações, descontos e reclamações. Embora não seja extremamente longo em quantidade de linhas, apresenta uma sequência extensa de tarefas diferentes.

### 6. Duplicated Code (Código Duplicado)

**Localização:** Método `duplicateMethod()`.

**Trecho:**
    public void duplicateMethod() {
        this.createOrder("Cola");
        this.createOrder("Cola");
    }

**Justificativa:** A mesma instrução é repetida consecutivamente, sem apresentar diferenças de comportamento ou parâmetros, caracterizando duplicação de código.

### 7. Switch Statements / Repeated Switches (Condicionais Repetitivas)

**Localização:** Método `handleComplaint()`.

**Trecho:**
    if (complaint.equals("cold drink")) {
        System.out.println("Handling complaint: Drink is cold");
    } else if (complaint.equals("wrong drink")) {
        System.out.println("Handling complaint: Wrong drink delivered");
    } else {
        System.out.println("Handling complaint: General complaint");
    }

**Justificativa:** O método utiliza uma estrutura condicional para distinguir tipos de reclamações com base em valores textuais. Essa estrutura apresenta uma seleção de comportamentos por tipo, embora não exista evidência de repetição da mesma lógica em outros métodos, requisito importante para caracterizar Repeated Switches na segunda edição de Fowler.

### 8. Middle Man (Intermediário)

**Localização:** Método `middleMethod()`.

**Trecho:**
    public void middleMethod() {
        System.out.println("Middleman method delegating to another method");
        this.realMethod();
    }

**Justificativa:** O método desempenha principalmente o papel de intermediário entre `middlemanMethod()` e `realMethod()`, encaminhando a execução para outro método sem acrescentar lógica de negócio significativa.

### 9. Speculative Generality (Generalidade Especulativa)

**Localização:** Métodos `anotherUnusedMethod()`, `yetAnotherUnusedMethod()` e `refusedBequest()`.

**Trecho:**
    public void anotherUnusedMethod() {
    }

    public void yetAnotherUnusedMethod() {
    }

    public void refusedBequest() {
    }

**Justificativa:** Os três métodos possuem implementações vazias e não são chamados por outros métodos no código apresentado. Isso sugere a existência de funcionalidades sem propósito atual demonstrável, compatível com o code smell Speculative Generality.

---

## Resumo dos Code Smells Identificados

| Code Smell | Localização |
|---|---|
| Data Clumps | Atributos do cliente e `updateCustomerInfo()` |
| Long Parameter List | `updateCustomerInfo()` |
| Temporary Field | `tempDiscountCode`, `tempOrderNote` |
| Large Class | Classe `Drink` |
| Long Method | `longMethod()` |
| Duplicated Code | `duplicateMethod()` |
| Switch Statements / Repeated Switches | `handleComplaint()` |
| Middle Man | `middleMethod()` |
| Speculative Generality | Três métodos vazios |

**Observação:** Nem todos os nove itens apresentam o mesmo grau de evidência. Temporary Field, Long Method, Repeated Switches e Speculative Generality são classificações possíveis, mas não totalmente confirmadas pelo trecho isolado. Em especial, campos não utilizados não são necessariamente temporários, e uma única sequência `if/else` não comprova Repeated Switches. Também não foram identificadas evidências suficientes para classificar `chainOfMethods()` como Message Chains, `accessInternalDetails()` como Inappropriate Intimacy ou `refusedBequest()` como Refused Bequest.