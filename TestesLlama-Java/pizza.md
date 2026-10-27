# Análise de Code Smells — Classe `Pizza` e Subclasses

Código do dataset de "smelly code" disponibilizado por Ahmed R. Sadik (Honda Research Institute Europe GmbH). Segue o levantamento dos code smells efetivamente presentes.

---

## 1. Classes com responsabilidades excessivas / falta de coesão

### 1.1 **God Class / Large Class**
**Onde:** classe `Pizza` como um todo.

**Justificativa:** a classe concentra múltiplas responsabilidades distintas que não pertencem ao conceito de "pizza": estado e comportamento do produto (tamanho, massa, cobertura, queijo extra), dados pessoais do cliente (nome, endereço, telefone, e-mail), funcionalidades de marketing (`notifyForPromotion`, `notifyForDiscount`, `notifyForNewArrivals`), fidelidade/descontos (`applyDiscount`, `applyLoyaltyPoints`), atendimento/CRM (`handleComplaint`, `askForReceipt`) e o processo de pedido. Uma classe que acumula dados do produto e do cliente ao mesmo tempo evidencia essa acumulação de responsabilidades.

### 1.2 **Divergent Change (mudança divergente)**
**Onde:** classe `Pizza` como um todo.

**Justificativa:** existem pelo menos eixos de mudança independentes que forçariam alterações na mesma classe: alterar a política de descontos/fidelidade, alterar a forma de notificação ao cliente, alterar o tratamento de reclamações e alterar atributos do produto. Um único arquivo/classe teria que ser modificado por razões completamente diferentes.

### 1.3 **Shotgun Surgery (cirurgia de espingarda)**
**Onde:** dados do cliente replicados em vários métodos — `updateCustomerInfo`, `updateCustomerName`, `updateCustomerAddress`, `updateCustomerPhoneNumber`, `updateCustomerEmail`.

**Justificativa:** qualquer mudança na representação dos dados do cliente (ex.: adicionar/renomear um campo) obriga a alterar vários métodos que tocam nos mesmos atributos `customer*`, caracterizando mudança espalhada por diversos pontos.

---

## 2. Duplicação

### 2.1 **Duplicated Code (código duplicado)**
**Onde:**
- `updateCustomerInfo` vs. `updateCustomerName` — ambos atribuem `customerFirstName` e `customerLastName` com o mesmo par de instruções.
- `updateCustomerAddress`, `updateCustomerPhoneNumber` e `updateCustomerEmail` — todos repetem o mesmo padrão de atribuição simples a um único campo.
- Classe `duplicateMethod`: há instrução idêntica repetida literalmente duas vezes (`this.setTopping("Cheese");`).

**Justificativa:** trechos de código com estrutura/lógica equivalente aparecem replicados, o que leva a manutenção duplicada (corrigir em um lugar e esquecer o outro).

### 2.2 **Duplicated Code (atribuição redundante)**
**Onde:** método `duplicateMethod`.

**Justificativa:** além da duplicação estrutural citada, há uma atribuição redundante consecutiva do mesmo valor ao mesmo campo (`setTopping("Cheese")` duas vezes seguidas), código efetivamente inútil/duplicado.

---

## 3. Métodos problemáticos

### 3.1 **Long Method (método longo)**
**Onde:** método `longMethod`.

**Justificativa:** o método executa uma sequência extensa de operações heterogêneas (configurar tamanho/massa/cobertura, atualizar dados do cliente, disparar notificações, aplicar desconto, aplicar fidelidade e tratar reclamação) acumulando muitos passos e responsabilidades em um único corpo. O próprio nome do método explicita o problema.

### 3.2 **Long Parameter List (lista de parâmetros longa)**
**Onde:**
- `updateCustomerInfo(String firstName, String lastName, String address, String phoneNumber, String email)` — 5 parâmetros.
- `orderWithUnnecessaryDetails(String pizzaType, String size, String crustType, String toppings, boolean extraCheese, String discountCode)` — 6 parâmetros.

**Justificativa:** métodos com muitos parâmetros dificultam leitura, chamada e manutenção; o agrupamento desses dados em um objeto seria mais coeso (apenas diagnóstico, sem propor refatoração).

### 3.3 **Flag Argument (parâmetro bandeira)**
**Onde:** `orderWithUnnecessaryDetails(..., boolean extraCheese, ...)`.

**Justificativa:** o parâmetro booleano `extraCheese` funciona como "bandeira" para alternar comportamento/estado, o que torna a chamada pouco expressiva e sinaliza que o método atende a mais de uma variação.

### 3.4 **Dead Code / Unused (métodos não utilizados)**
**Onde:** `anotherUnusedMethod`, `yetAnotherUnusedMethod`.

**Justificativa:** os métodos estão vazios, não são chamados em nenhum ponto do código e os próprios nomes ("unused") indicam que são código morto mantido na classe.

### 3.5 **Empty Method / Refused Bequest**
**Onde:** `refusedBequest()` (vazio) e também `anotherUnusedMethod`/`yetAnotherUnusedMethod`.

**Justificativa:** `refusedBequest` é um método vazio que a subclasse herda mas não utiliza/implementa, indicando que a herança é rejeitada — comportamento típico de *Refused Bequest*. Os métodos vazios não usados reforçam a presença de métodos ocos.

### 3.6 **Comments como desculpa para código ruim / excesso de `System.out.println`** *(observação de estilo)*
**Onde:** muitos métodos (`notifyForPromotion`, `notifyForDiscount`, `notifyForNewArrivals`, `applyDiscount`, `applyLoyaltyPoints`, `handleComplaint`, `askForReceipt`, etc.).

**Justificativa:** os métodos usam `System.out.println` por toda parte como forma de "implementação", o que evidencia código provisório/placeholder em vez de comportamento real. Em conjunto com nomes como `middleMethod`/`realMethod`, sinaliza estrutura artificial.

---

## 4. Acoplamento / delegação

### 4.1 **Middle Man (intermediário)**
**Onde:** `middlemanMethod` → `middleMethod` → `realMethod`.

**Justificativa:** `middlemanMethod` apenas delega para `middleMethod`, que por sua vez apenas delega para `realMethod`, sem adicionar valor próprio. A classe encadeia intermediários que só repassam chamadas.

### 4.2 **Message Chain (cadeia de mensagens)**
**Onde:** `chainOfMethods` — em conjunto com `updateCustomerAddress`.

**Justificativa:** o método é descrito como "iniciando uma cadeia de mensagens" e realiza uma chamada que percorre múltiplos objetos/etapas para obter/atualizar um dado, caracterizando uma cadeia de mensagens longa.

### 4.3 **Inappropriate Intimacy (intimidade inapropriada)**
**Onde:** `accessInternalDetails()` — acessa diretamente `this.size`, `this.doughType`, `this.topping`.

**Justificativa:** o método expõe/consome diretamente detalhes internos do objeto (campos privados) de forma que quebra o encapsulamento esperado, demonstrando alto acoplamento com a representação interna.

---

## 5. Problemas na hierarquia de herança

### 5.1 **Refused Bequest (rejeição de herança)**
**Onde:** subclasses `CheesePizza`, `VeggiePizza`, `TunaPizza`, `PepperoniPizza`.

**Justificativa:** as subclasses apenas definem valores de construtor (`super(...)`) e não compartilham/utilizam a maior parte do comportamento da superclasse (dados do cliente, notificações, reclamações, descontos). Elas herdam um conjunto enorme de métodos que não lhes cabe usar — herança inadequada/rejeitada.
- Agravante em `CheesePizza`: sobrescreve `handleComplaint` apenas para um caso especial e delega o resto a `super`, evidência de que a hierarquia não é natural.

### 5.2 **Lazy Class / classe com pouco valor**
**Onde:** `VeggiePizza`, `TunaPizza`, `PepperoniPizza`.

**Justificativa:** essas subclasses só inicializam a superclasse com valores fixos e nada mais adicionam (nenhum atributo ou comportamento próprio), agregando pouco ou nenhum valor — sintoma de *Lazy Class*.

---

## 6. Métodos com nomes/design ruins

### 6.1 **Métodos com nomes enganosos/genéricos**
**Onde:** `middleMethod`, `realMethod`, `middlemanMethod`, `chainOfMethods`, `orderWithUnnecessaryDetails`, `duplicateMethod`, `longMethod`, `refusedBequest`, `anotherUnusedMethod`, `yetAnotherUnusedMethod`.

**Justificativa:** os nomes descrevem o "smell" ou a posição estrutural, e não a intenção de negócio, o que prejudica legibilidade e indica design artificial/didático em vez de código orientado ao domínio.

### 6.2 **Campo temporário / não encapsulado**
**Onde:** atributos `tempDiscountCode` e `tempOrderNote`.

**Justificativa:** os campos prefixados com `temp*` são declarados mas nunca utilizados/gerenciados por nenhum método da classe, evidenciando estado temporário "morto" dentro da classe (dados órfãos).

---

## 7. Tratamento de variação com condicionais

### 7.1 **Switch Statements / condicionais longas**
**Onde:** `handleComplaint(String complaint)` (cadeia de `if/else if/else`), replicada também em `CheesePizza` (com novo `if` + `super`).

**Justificativa:** o comportamento varia por tipo de reclamação usando uma cadeia de condicionais, e esse mesmo estilo é estendido nas subclasses, caracterizando variação por tipo implementada com `switch/if` em vez de polimorfismo.

---

## Resumo (checklist)

| # | Code Smell | Onde |
|---|-----------|------|
| 1 | God/Large Class | classe `Pizza` |
| 2 | Divergent Change | classe `Pizza` |
| 3 | Shotgun Surgery | métodos `updateCustomer*` |
| 4 | Duplicated Code | `updateCustomerInfo`/`updateCustomerName`, `duplicateMethod`, `updateCustomerAddress/Phone/Email` |
| 5 | Long Method | `longMethod` |
| 6 | Long Parameter List | `updateCustomerInfo`, `orderWithUnnecessaryDetails` |
| 7 | Flag Argument | `orderWithUnnecessaryDetails` (`extraCheese`) |
| 8 | Dead Code | `anotherUnusedMethod`, `yetAnotherUnusedMethod` |
| 9 | Empty Method / Refused Bequest | `refusedBequest()` |
| 10 | Middle Man | `middlemanMethod`/`middleMethod` |
| 11 | Message Chain | `chainOfMethods` |
| 12 | Inappropriate Intimacy | `accessInternalDetails` |
| 13 | Refused Bequest | subclasses de `Pizza` |
| 14 | Lazy Class | `VeggiePizza`, `TunaPizza`, `PepperoniPizza` |
| 15 | Switch/If-cadeia | `handleComplaint` |
| 16 | Campos órfãos/temporários | `tempDiscountCode`, `tempOrderNote` |
| 17 | Nomes ruins/artificiais | vários (`middleMethod`, `realMethod`, etc.) |

Conforme solicitado, foram listados apenas os smells presentes, com localização e justificativa, sem propor refatorações.