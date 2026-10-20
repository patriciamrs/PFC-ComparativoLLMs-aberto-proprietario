## Análise de Code Smells – Classe Shop

### 1. Large Class (Classe Grande)

**Localização:** Classe `Shop`.

**Justificativa:** A classe concentra diversas responsabilidades, incluindo criação de pizzas, gerenciamento de pedidos, armazenamento de informações de clientes, aplicação de descontos, notificações, tratamento de reclamações e acesso a informações da cozinha. Essa concentração caracteriza uma classe com responsabilidades excessivas.

### 2. Long Method (Método Longo)

**Localização:** Método `long_method()`.

**Justificativa:** O método executa uma sequência extensa de operações relacionadas a diferentes responsabilidades, como atualização de dados de clientes, notificações, descontos, reclamações e acesso a informações internas, concentrando diversas tarefas em um único método.

### 3. Data Clumps (Agrupamento de Dados)

**Localização:** Atributos `first_name`, `last_name`, `address`, `phone_number` e `email`, além do método `update_contact_info()`.

**Justificativa:** Os atributos representam um conjunto de informações relacionadas ao cliente e aparecem agrupados tanto na classe quanto nos parâmetros do método. Essa repetição de dados relacionados caracteriza o code smell Data Clumps.

### 4. Temporary Field (Campo Temporário)

**Localização:** Atributos `temp_discount_code` e `temp_order_note` no construtor `__init__()`.

**Justificativa:** Os atributos são inicializados com `None` e não são utilizados pelos demais métodos da classe. Sua presença sugere campos destinados a situações específicas, permanecendo sem utilização durante o funcionamento apresentado.

### 5. Dead Code (Código Morto)

**Localização:** Métodos `another_unused_method()` e `yet_another_unused_method()`.

**Justificativa:** Ambos os métodos possuem apenas a instrução `pass`, não apresentam comportamento implementado e não são chamados em nenhum trecho do código apresentado.

### 6. Switch Statements (Instruções Condicionais)

**Localização:** Método `create_pizza()`.

**Justificativa:** O método utiliza uma sequência de condições `if` e `elif` para identificar o tipo de pizza e instanciar classes diferentes. Essa estrutura representa uma seleção de comportamentos baseada em valores específicos de uma variável.

### 7. Duplicated Code (Código Duplicado)

**Localização:** Método `handle_complaint()`.

**Justificativa:** Todas as condições executam exatamente a mesma instrução, `self.casher.calm_customer_down()`, independentemente do tipo de reclamação. Isso caracteriza duplicação de comportamento em diferentes ramificações condicionais.

### 8. Message Chains (Cadeia de Mensagens)

**Localização:** Métodos `chain_of_methods()` e `access_internal_details()`.

**Justificativa:** Os métodos acessam objetos por meio de uma sequência de referências, como `self.casher.chef.clean_kitchen()` e `self.casher.chef.busy`. Isso demonstra que a classe `Shop` navega por objetos intermediários para acessar comportamentos e informações de outros objetos.

### 9. Middle Man (Intermediário)

**Localização:** Métodos `middleman_method()` e `middle_method()`.

**Justificativa:** Os métodos atuam como intermediários na execução de `real_method()`, realizando chamadas sucessivas sem acrescentar lógica significativa ao processamento. Essa delegação desnecessária caracteriza o code smell Middle Man.

### 10. Inappropriate Intimacy (Intimidade Inapropriada)

**Localização:** Método `access_internal_details()`.

**Justificativa:** O método acessa diretamente o atributo `busy` do objeto `Chef` por meio de `self.casher.chef.busy`. Esse acesso demonstra conhecimento sobre detalhes internos de outra classe, indicando acoplamento entre os objetos.

### 11. Long Parameter List (Lista Longa de Parâmetros)

**Localização:** Método `update_contact_info()`.

**Justificativa:** O método recebe cinco parâmetros relacionados às informações pessoais e de contato do cliente (`first_name`, `last_name`, `address`, `phone_number` e `email`), caracterizando uma lista relativamente extensa de parâmetros que representam um mesmo conjunto de dados.

### 12. Primitive Obsession (Obsessão por Tipos Primitivos)

**Localização:** Método `create_pizza()` e atributos relacionados ao cliente.

**Justificativa:** O método `create_pizza()` utiliza valores de texto, como `"Cheese"`, `"Veggie"`, `"Tuna"` e `"Pepperoni"`, para representar diferentes tipos de pizza e determinar o comportamento do sistema. Além disso, informações relacionadas ao cliente são armazenadas individualmente em atributos de tipos primitivos, em vez de serem representadas por uma estrutura específica do domínio.

---

**Observação:** A identificação de alguns code smells depende do contexto de utilização. Por exemplo, os campos `temp_discount_code` e `temp_order_note` são candidatos a *Temporary Field*, mas o código apresentado não demonstra que sejam utilizados apenas em determinadas circunstâncias. Da mesma forma, métodos com `pass` são comprovadamente vazios, mas não é possível afirmar que não sejam utilizados em outros arquivos. Essas classificações devem ser consideradas com essa ressalva.