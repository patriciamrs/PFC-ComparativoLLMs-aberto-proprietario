# Análise de Code Smells — Classe `Customer`

A classe `Customer` apresenta uma grande quantidade de code smells, muitos deles propositalmente inseridos (o cabeçalho do arquivo indica que é um dataset de código "smelly" para pesquisa e refatoração). A seguir, apresento cada ocorrência em texto corrido.

**Dead Code (Código Morto) e Empty Method (Métodos Vazios).** O método `anotherUnusedMethod()` é declarado com o corpo completamente vazio e não é chamado por ninguém, configurando código morto. O mesmo ocorre com `refusedBequest()`, que também é um método vazio, sem implementação e sem uso — embora o nome remeta ao smell "Refused Bequest", aqui o efeito concreto é o de código morto. De forma semelhante, `middleMethod()` e `realMethod()`, além de `askForReceipt()`, existem apenas para imprimir mensagens triviais, sem lógica de negócio real e sem contribuição funcional ao comportamento da classe.

**Middle Man (Homem do Meio).** O método `middleMethod()` apenas delega a chamada para `realMethod()`, sem acrescentar nenhum comportamento próprio. Da mesma forma, `middlemanMethod()` chama `middleMethod()`, que por sua vez chama `realMethod()`, criando uma corrente de delegação desnecessária. Essa delegação em excesso caracteriza o smell de Middle Man.

**Message Chain / Chain of Methods (Cadeia de Mensagens).** No método `chainOfMethods()`, a chamada `this.pizzaShop.getCashier().getChef().cleanKitchen()` percorre uma cadeia profunda de objetos, criando forte acoplamento com a estrutura interna da `Shop`. O mesmo padrão aparece em `accessInternalDetails()`, com `pizzaShop.getCashier().getChef().isBusy()`.

**Long Method (Método Longo).** O método `longComplaintMethod()` concentra seis chamadas a `complain()` seguidas de `askForReceipt()` em um único bloco, acumulando muitas instruções repetitivas. Já `orderWithUnnecessaryDetails(...)` também é extenso, misturando impressão de mensagem e chamada de outro método com muitos parâmetros.

**Long Parameter List (Lista Longa de Parâmetros).** `orderWithUnnecessaryDetails(...)` recebe seis parâmetros (`pizzaType`, `size`, `crustType`, `toppings`, `extraCheese`, `discountCode`), a maioria dos quais apenas é impressa e não participa da lógica. O método `updateContactInfo(...)` recebe cinco parâmetros (`firstName`, `lastName`, `address`, `phoneNumber`, `email`), que espelham campos individuais que já possuem métodos `update...` próprios.

**Duplicate Code (Código Duplicado).** Em `duplicateComplaint()`, as chamadas `complain("Pizza is cold")` e `complain("Pizza is late")` aparecem repetidas duas vezes cada. O mesmo padrão de instruções repetidas (`this.complain(...)`) reaparece em `longComplaintMethod()`, caracterizando duplicação de estrutura.

**Inappropriate Intimacy (Intimidade Inapropriada) / Feature Envy.** Em `accessInternalDetails()`, o objeto acessa detalhes internos de outro (`getCashier().getChef().isBusy()`), demonstrando acoplamento excessivo entre classes. O mesmo fenômeno ocorre em `complain()` e `chainOfMethods()`, que penetram na estrutura interna da `Shop` via `getCashier()`.

**Dispersed Coupling (Acoplamento Disperso).** O caminho de dependência `pizzaShop.getCashier()` é reutilizado em vários métodos distintos, espalhando o acoplamento pela classe inteira em vez de concentrá-lo em um ponto.

**Primitive Obsession (Obsessão por Primitivos).** Praticamente todos os atributos da classe são primitivos ou `String`: `firstName`, `lastName`, `address`, `phoneNumber`, `email`, `tempDiscountCode`, `tempOrderNote` e o `boolean frequentCustomerDiscount`. Conceitos ricos como endereço, telefone e e-mail são representados por tipos simples, em vez de objetos de valor.

**Temporary Field (Campo Temporário).** Os atributos `tempDiscountCode` e `tempOrderNote` são declarados com o prefixo "temp" e existem apenas para uso temporário e condicional, tendendo a ficar vazios na maior parte do tempo de vida do objeto.

**Switch Statements / Cadeia de Condicionais.** No método `handleComplaint(String complaint)`, há uma sequência extensa de `if / else if` comparando strings (`"cold pizza"`, `"late delivery"`, `"wrong order"`) para decidir o comportamento, sem uso de polimorfismo.

**Data Class (Classe Anêmica).** Como um todo, a classe `Customer` funciona em boa parte como um recipiente de dados, expondo campos por meio de vários métodos `update...` (`updateName`, `updateAddress`, `updatePhoneNumber`, `updateEmail`, além de `updateContactInfo`), com pouca lógica de negócio significativa.

**Speculative Generality (Generalidade Especulativa).** Os métodos `notifyForPromotion()`, `notifyForDiscount()`, `notifyForNewArrivals()`, `applyDiscount()` e `applyLoyaltyPoints()` parecem criados para um uso futuro hipotético, mas apenas imprimem mensagens e não são chamados em nenhum lugar.

**Bad Naming (Nomenclatura Inadequada).** Nomes como `middleMethod()`, `anotherUnusedMethod()` e `refusedBequest()` são genéricos ou até nomeiam o próprio smell, sem significado de domínio claro.

**Violação da Lei de Demeter.** Tanto `accessInternalDetails()` quanto `chainOfMethods()` chamam métodos de objetos obtidos por meio de outros métodos (`getCashier().getChef()...`), violando o princípio de "falar apenas com amigos diretos".

Em resumo, os smells presentes incluem: Dead Code / Empty Method, Middle Man, Message Chain, Long Method, Long Parameter List, Duplicate Code, Inappropriate Intimacy (com indícios de Feature Envy), Dispersed Coupling, Primitive Obsession, Temporary Field, Switch Statements (cadeia de condicionais), Data Class anêmica, Speculative Generality, Bad Naming e violação da Lei de Demeter. Conforme solicitado, não foram propostas refatorações nem alterações na implementação.