# Análise de Code Smells — Classe `Cashier`

Segue o levantamento dos code smells presentes no código, descritos em texto corrido.

---

**Large Class (Classe Grande).** Ocorre na classe `Cashier` como um todo. A classe acumula responsabilidades muito distintas e pouco relacionadas entre si: o atendimento ao cliente (em métodos como `takeOrder` e `deliverPizzaToCustomer`), a comunicação de promoções e avisos (`notifyForPromotion`, `notifyForDiscount`, `notifyForNewArrivals`), o armazenamento dos dados cadastrais do cliente (`firstName`, `lastName`, `address`, `phoneNumber`, `email`, além de todos os `update*`) e também o tratamento de reclamações. Essa concentração de papéis num único ponto evidencia uma classe grande demais e com baixa coesão.

**Feature Envy (Inveja de Funcionalidade).** Ocorre nos métodos `takeOrder`, `hurryUpChef`, `calmCustomerDown` e `chainOfMethods`. Nesses métodos, o Cashier apenas imprime uma mensagem sobre sua própria ação, mas a lógica real é sempre delegada ao objeto `chef` (por meio de `this.chef.bakePizza(...)`, `this.chef.hurryUp()` e `this.chef.cleanKitchen()`). Ou seja, a classe demonstra interesse desproporcional no comportamento e nos dados de `Chef`, "invejando" uma funcionalidade que não é dela.

**Inappropriate Intimacy (Intimidade Inadequada).** Ocorre na relação entre `Cashier` e `Chef`, especialmente em `chainOfMethods` e em `accessInternalDetails`. Existe um forte acoplamento entre as duas classes, já que `Cashier` aciona diretamente métodos internos de `Chef` (`bakePizza`, `hurryUp`, `cleanKitchen`, `isBusy`), criando dependência excessiva sobre os detalhes internos de outra classe. O método `accessInternalDetails`, em particular, chega a acessar e imprimir o estado interno de `Chef` via `chef.isBusy()`.

**Divergent Change (Mudança Divergente).** Ocorre na estrutura geral da classe. Há vários motivos independentes que poderiam forçar alterações na mesma classe: mudanças no cadastro do cliente, mudanças no fluxo de notificações e promoções, mudanças na interação com o Chef e mudanças no tratamento de reclamações. Qualquer alteração em um desses eixos obriga a modificar `Cashier`, caracterizando múltiplas razões de mudança concentradas numa única classe.

**Long Method (Método Longo).** Ocorre no método `longMethod()`. Ele executa, num único bloco sequencial, diversas tarefas distintas — chama `takeOrder("Cheese")`, `hurryUpChef()`, `calmCustomerDown()`, `deliverPizzaToCustomer()` e `askForReceipt()` — o que torna o método longo e responsável por muitos passos de uma só vez.

**Duplicated Code (Código Duplicado).** Ocorre no método `duplicateMethod()`, que chama `this.takeOrder("Cheese")` duas vezes seguidas com o mesmo argumento, repetindo literalmente a mesma instrução.

**Duplicated Code (duplicação nos ramos de decisão).** Ocorre no método `handleComplaint(String complaint)`. Todos os ramos do encadeamento `if / else if / else` executam exatamente a mesma chamada `this.calmCustomerDown()`, independentemente do valor recebido em `complaint`. O comportamento é duplicado em todos os ramos, tornando a distinção entre eles inútil.

**Message Chain (Cadeia de Mensagens).** Ocorre no método `chainOfMethods()`. O próprio código indica que está "iniciando uma cadeia de mensagens", acessando o objeto `chef` para acionar diretamente seu comportamento (`this.chef.cleanKitchen()`), o que caracteriza a navegação por mensagens encadeadas entre objetos.

**Middle Man (Homem do Meio).** Ocorre nos métodos `middlemanMethod()` e `middleMethod()`. O `middlemanMethod()` apenas chama `middleMethod()`, que por sua vez apenas chama `realMethod()`. Nenhum dos dois intermediários acrescenta lógica real própria, atuando somente como camadas de delegação sem valor.

**Dead Code / Métodos Vazios.** Ocorre em `anotherUnusedMethod()` e `refusedBequest()`. Ambos são métodos totalmente vazios, sem corpo e sem uso aparente, não executando nenhuma ação.

**Getter não utilizado.** Ocorre em `getChef()`. O método expõe o objeto `chef` sem uso interno evidente, contribuindo para a exposição desnecessária do estado interno da classe.

**Data Class (Classe de Dados) — tendência nos atributos do cliente.** Ocorre no conjunto de atributos `firstName`, `lastName`, `address`, `phoneNumber` e `email`, juntamente com os métodos de atualização (`updateName`, `updateAddress`, `updatePhoneNumber`, `updateEmail` e `updateContactInfo`). Esses campos existem quase exclusivamente para armazenar e atualizar dados do cliente, comportamento típico de uma classe de dados embutida.

**Long Parameter List (Lista de Parâmetros Longa).** Ocorre no método `updateContactInfo(String firstName, String lastName, String address, String phoneNumber, String email)`. O método recebe cinco parâmetros diretamente, o que dificulta a leitura, a chamada e a manutenção do método.

**Speculative Generality / Atributos não utilizados.** Ocorre nos atributos `tempDiscountCode` e `tempOrderNote`, que são declarados mas nunca lidos nem escritos em nenhum método da classe. São campos "temporários" criados para necessidades que não existem no código atual.

**Atributo não utilizado.** Ocorre no campo `frequentCustomerDiscount`. Ele é inicializado no construtor com `false`, mas nunca é consultado nem alterado em qualquer método, indicando um dado sem utilidade efetiva.

**Comportamento enganoso (lógica que não corresponde ao nome).** Ocorre nos métodos `applyDiscount()` e `applyLoyaltyPoints()`. Ambos executam apenas um `System.out.println`, sem implementar de fato o que seus nomes prometem, configurando comportamento enganoso em relação à intenção declarada.

---

### Observação complementar

O método `refusedBequest()` tem esse nome remetendo ao smell **Refused Bequest (Herança Recusada)**, porém, no código apresentado, `Cashier` não herda de nenhuma classe, portanto o smell de herança propriamente dito não se configura — o que existe ali é um método vazio sem uso. Registro isso para não atribuir o smell de herança indevidamente.

### Resumo dos smells identificados

Large Class (`Cashier`); Feature Envy (`takeOrder`, `hurryUpChef`, `calmCustomerDown`, `chainOfMethods`); Inappropriate Intimacy (`Cashier` ↔ `Chef`, `accessInternalDetails`, `chainOfMethods`); Divergent Change (estrutura geral); Long Method (`longMethod()`); Duplicated Code (`duplicateMethod()` e ramos redundantes de `handleComplaint()`); Message Chain (`chainOfMethods()`); Middle Man (`middlemanMethod()` / `middleMethod()`); Dead Code / métodos vazios (`anotherUnusedMethod()`, `refusedBequest()`); getter não utilizado (`getChef()`); Data Class (atributos do cliente); Long Parameter List (`updateContactInfo(...)`); atributos não utilizados (`tempDiscountCode`, `tempOrderNote`, `frequentCustomerDiscount`); e comportamento enganoso (`applyDiscount()`, `applyLoyaltyPoints()`).

Conforme solicitado, nenhuma refatoração ou alteração de implementação foi proposta — apenas a identificação e a justificativa dos code smells presentes.