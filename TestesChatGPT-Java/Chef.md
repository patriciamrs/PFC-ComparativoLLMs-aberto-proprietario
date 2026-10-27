## Análise de Code Smells – Classe Chef (Java)

### 1. Large Class (Classe Grande)
- **Localização:** Classe `Chef`.
- **Justificativa:** A classe concentra diversas responsabilidades, como preparação de pizzas, limpeza da cozinha, gerenciamento de informações de contato, notificações promocionais, aplicação de descontos e tratamento de reclamações. Essa quantidade de responsabilidades distintas indica uma classe excessivamente abrangente.

### 2. Long Method (Método Longo)
- **Localização:** Método `longMethod()`.
- **Justificativa:** O método executa uma sequência extensa de operações relacionadas a diferentes responsabilidades, incluindo preparação de pizzas, atualização de contatos, notificações, descontos e reclamações. Essa concentração de tarefas dificulta a compreensão e a manutenção do método.

### 3. Data Clumps (Agrupamento de Dados)
- **Localização:** Atributos `firstName`, `lastName`, `address`, `phoneNumber` e `email`, além do método `updateContactInfo()`.
- **Justificativa:** Os atributos representam um conjunto de informações pessoais relacionadas, sendo manipulados em conjunto pelo método `updateContactInfo()`. Esse agrupamento de dados indica a presença de Data Clumps.

### 4. Long Parameter List (Lista Longa de Parâmetros)
- **Localização:** Método `updateContactInfo(String firstName, String lastName, String address, String phoneNumber, String email)`.
- **Justificativa:** O método recebe cinco parâmetros relacionados às informações de contato. A quantidade de argumentos aumenta a complexidade da chamada e indica uma lista extensa de parâmetros.

### 5. Shotgun Surgery (Alterações Espalhadas)
- **Localização:** Métodos `updateContactInfo()`, `updateName()`, `updateAddress()`, `updatePhoneNumber()` e `updateEmail()`.
- **Justificativa:** A classe possui diferentes métodos responsáveis pela atualização das informações de contato. Entretanto, apenas essa separação não comprova Shotgun Surgery, pois seria necessário demonstrar que uma única mudança de requisito exigiria alterações em vários métodos. Portanto, não é possível confirmar esse smell apenas pelo código apresentado.

### 6. Feature Envy (Inveja de Funcionalidade)
- **Localização:** Método `accessInternalDetails()`.
- **Justificativa:** O método acessa informações do objeto `Pizza` por meio de `this.pizza.getTopping()`. Contudo, uma única consulta a outra classe não demonstra dependência excessiva de dados externos. Assim, não há evidência suficiente para confirmar Feature Envy.

### 7. Dead Code (Código Morto)
- **Localização:** Métodos `anotherUnusedMethod()`, `yetAnotherUnusedMethod()` e `refusedBequest()`.
- **Justificativa:** Os três métodos possuem implementações vazias, sem executar qualquer operação. Por não apresentarem comportamento funcional, constituem indícios de código desnecessário. A ausência de chamadas, entretanto, não pode ser comprovada sem analisar o restante do projeto.

### 8. Divergent Change (Mudança Divergente)
- **Localização:** Classe `Chef`.
- **Justificativa:** A classe reúne funcionalidades de diferentes áreas, como preparação de alimentos, informações de contato, marketing, descontos e atendimento ao cliente. Dessa forma, diferentes tipos de alterações nos requisitos podem exigir modificações na mesma classe por motivos distintos.

### 9. Middle Man (Intermediário)
- **Localização:** Métodos `middlemanMethod()` e `middleMethod()`.
- **Justificativa:** Os métodos realizam principalmente chamadas intermediárias para outros métodos, sem acrescentar processamento significativo. `middlemanMethod()` chama `middleMethod()`, que, por sua vez, chama `realMethod()`, criando níveis de delegação desnecessários.

### 10. Duplicate Code (Código Duplicado)
- **Localização:** Método `duplicateMethod()`.
- **Justificativa:** O método apresenta duas chamadas idênticas e consecutivas a `this.bakePizza("Cheese")`. Embora isso possa indicar redundância, não é suficiente para caracterizar o Duplicate Code de Fowler, pois as chamadas podem representar duas operações intencionais e não há duplicação de implementação.

### 11. Temporary Field (Campo Temporário)
- **Localização:** Atributos `tempDiscountCode` e `tempOrderNote`.
- **Justificativa:** Os atributos são declarados na classe, mas não são inicializados nem utilizados pelos métodos apresentados. Seus nomes sugerem informações temporárias, porém não há evidência de que sejam usados apenas em determinadas circunstâncias. Assim, a presença de Temporary Field não pode ser confirmada.

### 12. Speculative Generality (Generalidade Especulativa)
- **Localização:** Métodos `anotherUnusedMethod()`, `yetAnotherUnusedMethod()` e `refusedBequest()`.
- **Justificativa:** Os métodos são declarados sem implementação e não apresentam utilidade no trecho analisado. Isso pode indicar funcionalidades adicionadas sem uma necessidade concreta, caracterizando um possível caso de generalidade especulativa.

---

**Observação:** Os smells mais claramente sustentados pelo código são Large Class, Long Method, Middle Man e Divergent Change. Long Parameter List, Data Clumps e Speculative Generality também possuem indícios, mas dependem de critérios de avaliação. Os itens identificados como não confirmados não devem ser contabilizados como ocorrências comprovadas.
