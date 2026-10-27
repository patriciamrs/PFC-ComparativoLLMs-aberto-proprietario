# Análise de Code Smells — Pizza.java

## 1. Large Class (Classe Grande)

**Localização:** Classe `Pizza`.

**Justificativa:** A classe apresenta muitas responsabilidades, incluindo configuração de pizzas, armazenamento de informações de clientes, notificações promocionais, aplicação de descontos, tratamento de reclamações e gerenciamento de pedidos. Essa concentração de funcionalidades distintas caracteriza uma classe com responsabilidades excessivas.

## 2. Long Method (Método Longo)

**Localização:** Método `longMethod()`.

**Justificativa:** O método concentra diversas operações de naturezas diferentes, como configuração da pizza, atualização de dados do cliente, notificações, descontos e tratamento de reclamações. Apesar de não ser extremamente extenso em número de linhas, apresenta uma sequência de responsabilidades distintas.

## 3. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Métodos `orderWithUnnecessaryDetails()` e `updateCustomerInfo()`.

**Justificativa:** Os métodos recebem, respectivamente, seis e cinco parâmetros, exigindo o fornecimento de várias informações individuais em uma única chamada. Essa quantidade aumenta a complexidade de utilização e compreensão dos métodos.

## 4. Data Clumps (Agrupamentos de Dados)

**Localização:** Atributos `customerFirstName`, `customerLastName`, `customerAddress`, `customerPhoneNumber` e `customerEmail`, além dos métodos `updateCustomerInfo()` e `updateCustomerName()`.

**Justificativa:** Os atributos representam informações relacionadas a uma mesma entidade, o cliente, e aparecem agrupados na classe e em parâmetros de métodos. Essa associação recorrente caracteriza um conjunto de dados que possui significado em comum.

## 5. Dead Code (Código Morto)

**Localização:** Métodos `anotherUnusedMethod()`, `yetAnotherUnusedMethod()` e `refusedBequest()`.

**Justificativa:** Os métodos possuem corpos vazios e não executam nenhuma operação. Dessa forma, não apresentam comportamento funcional na implementação fornecida.

## 6. Duplicate Code (Código Duplicado)

**Localização:** Método `duplicateMethod()`.

**Justificativa:** O método apresenta duas chamadas consecutivas e idênticas a `setTopping("Cheese")`, realizando repetidamente a mesma operação sem necessidade aparente.

## 7. Switch Statements / Repeated Conditional Logic (Lógica Condicional)

**Localização:** Método `handleComplaint()`.

**Justificativa:** O método utiliza uma sequência de condições para determinar o comportamento com base no tipo de reclamação informado. Essa estrutura concentra diferentes comportamentos em uma cadeia de decisões condicionais.

## 8. Feature Envy (Inveja de Funcionalidade)

**Localização:** Métodos `updateCustomerInfo()`, `notifyForPromotion()`, `notifyForDiscount()`, `notifyForNewArrivals()`, `applyDiscount()` e `applyLoyaltyPoints()`.

**Justificativa:** Esses métodos representam operações relacionadas ao gerenciamento de clientes, promoções e benefícios comerciais, em vez de características próprias de uma pizza. Isso indica que a classe `Pizza` concentra comportamentos pertencentes a outros contextos de responsabilidade.

## 9. Middle Man (Intermediário)

**Localização:** Métodos `middlemanMethod()` e `middleMethod()`.

**Justificativa:** Os métodos atuam principalmente como intermediários, encaminhando a execução para outros métodos. Embora apresentem mensagens de saída, sua principal função é delegar chamadas, acrescentando níveis de indireção ao fluxo de execução.

## 10. Lazy Class (Classe Preguiçosa)

**Localização:** Classes `VeggiePizza`, `TunaPizza` e `PepperoniPizza`.

**Justificativa:** As subclasses apresentam implementações mínimas, limitadas aos construtores que definem valores específicos. Não possuem comportamentos próprios e dependem integralmente das funcionalidades herdadas de `Pizza`, apresentando pouca responsabilidade individual.

## 11. Primitive Obsession (Obsessão por Tipos Primitivos)

**Localização:** Atributos da classe `Pizza`, como `size`, `doughType`, `topping`, `customerAddress`, `customerPhoneNumber` e `customerEmail`.

**Justificativa:** O código utiliza diversas variáveis do tipo `String` para representar informações de domínio, como tamanho, tipo de massa, cobertura e dados de contato. Esses valores são tratados como textos simples, sem estruturas específicas que representem seus conceitos e restrições.
