# Análise de Code Smells — Classe Shop

### 1. Long Method (Método Longo)
- **Localização:** Método `long_method()`.
- **Justificativa:** O método executa diversas operações relacionadas a informações de contato, notificações, descontos, reclamações e acesso a objetos internos. A concentração de múltiplas responsabilidades em um único método aumenta sua complexidade e dificulta a compreensão e manutenção.

### 2. Large Class (Classe Grande)
- **Localização:** Classe `Shop`.
- **Justificativa:** A classe possui diversos atributos e métodos com responsabilidades distintas, como gerenciamento de pedidos, informações de clientes, promoções, descontos e reclamações. Essa concentração de funcionalidades caracteriza uma classe com responsabilidades excessivas.

### 3. Long Parameter List (Lista Longa de Parâmetros)
- **Localização:** Método `update_contact_info(first_name, last_name, address, phone_number, email)`.
- **Justificativa:** O método recebe cinco parâmetros relacionados às informações de contato do cliente, caracterizando uma lista relativamente extensa de argumentos e aumentando a complexidade da chamada.

### 4. Data Clumps (Agrupamentos de Dados)
- **Localização:** Atributos `first_name`, `last_name`, `address`, `phone_number` e `email`, além dos métodos `update_contact_info()` e `update_name()`.
- **Justificativa:** Os atributos representam informações relacionadas ao cliente e aparecem agrupados em diferentes partes do código. A recorrência desses dados sugere que formam um conjunto de informações associado a uma mesma entidade.

### 5. Duplicate Code (Código Duplicado)
- **Localização:** Método `handle_complaint()`.
- **Justificativa:** Todas as condições executam exatamente a mesma instrução, `self.casher.calm_customer_down()`, independentemente do tipo de reclamação. Essa repetição caracteriza duplicação de comportamento.

### 6. Message Chains (Cadeias de Mensagens)
- **Localização:** Métodos `chain_of_methods()` e `access_internal_details()`.
- **Trechos:**
  - `self.casher.chef.clean_kitchen()`
  - `self.casher.chef.busy`
- **Justificativa:** Os métodos acessam objetos por meio de uma sequência de referências, passando pelo atributo `casher` para alcançar o objeto `chef`. Isso demonstra dependência da estrutura interna de outros objetos.

### 7. Middle Man (Intermediário)
- **Localização:** Métodos `middleman_method()` e `middle_method()`.
- **Justificativa:** Os métodos atuam principalmente como intermediários, delegando a execução para outros métodos sem acrescentar comportamento significativo. Essa sequência de delegações introduz níveis adicionais de indireção.

### 8. Inappropriate Intimacy (Intimidade Inapropriada)
- **Localização:** Método `access_internal_details()`.
- **Trecho:** `self.casher.chef.busy`
- **Justificativa:** A classe `Shop` acessa diretamente o atributo `busy` do objeto `Chef`, por meio de `Cashier`, demonstrando conhecimento sobre detalhes internos de outra classe e aumentando o acoplamento entre elas.

### 9. Dead Code (Código Morto)
- **Localização:** Métodos `another_unused_method()` e `yet_another_unused_method()`.
- **Trechos:**
  - `def another_unused_method(self): pass`
  - `def yet_another_unused_method(self): pass`
- **Justificativa:** Os métodos não possuem implementação funcional e não são utilizados em nenhum ponto do código apresentado. São fortes indícios de código sem utilidade na implementação atual, embora a ausência de chamadas externas não possa ser comprovada apenas por esse arquivo.

### 10. Switch Statements / Repeated Switches (Condicionais Repetitivas)
- **Localização:** Métodos `create_pizza()` e `handle_complaint()`.
- **Justificativa:** O método `create_pizza()` utiliza uma sequência de condições `if/elif` para determinar qual tipo de pizza deve ser instanciado. Já `handle_complaint()` apresenta diversas condições para tipos de reclamação, embora todas executem a mesma operação. Essas estruturas representam decisões baseadas em valores específicos, mas não constituem, por si só, evidência de *Repeated Switches*, pois não há repetição da mesma lógica de seleção em diferentes pontos do código.

### 11. Speculative Generality (Generalidade Especulativa)
- **Localização:** Métodos `another_unused_method()` e `yet_another_unused_method()`.
- **Justificativa:** Os métodos foram declarados sem implementação e sem utilização visível. Podem indicar estruturas adicionadas para funcionalidades hipotéticas ou futuras, sem necessidade demonstrada no código atual. Entretanto, não é possível confirmar essa intenção apenas pelo trecho apresentado.

### 12. Temporary Field (Campo Temporário)
- **Localização:** Atributos `temp_discount_code` e `temp_order_note` no construtor `__init__()`.
- **Justificativa:** Os atributos são inicializados com `None` e não são utilizados nos métodos apresentados. Seus nomes sugerem armazenamento de informações temporárias que poderiam ser necessárias somente em determinadas circunstâncias. A caracterização como *Temporary Field*, porém, depende de evidências de que esses campos sejam utilizados apenas em situações específicas.
