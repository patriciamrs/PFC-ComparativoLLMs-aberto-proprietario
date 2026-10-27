# Análise de Code Smells — Código `Pizza`

Abaixo estão os code smells identificados, agrupados por tipo, com trecho/método/classe e justificativa.

---

## 1. Classe Grande (Large Class)
**Onde:** classe `Pizza`
**Justificativa:** A classe `Pizza` concentra responsabilidades muito distintas — dados do produto (tamanho, massa, cobertura), dados pessoais do cliente (`customer_first_name`, `customer_last_name`, `customer_address`, `customer_phone_number`, `customer_email`), comunicação/marketing, fidelidade, tratamento de reclamações e emissão de recibos. Isso viola o princípio da responsabilidade única.

---

## 2. Intimidade Inapropriada (Inappropriate Intimacy)
**Onde:** atributos de cliente (`customer_first_name`, `customer_last_name`, `customer_address`, `customer_phone_number`, `customer_email`) dentro de `Pizza`.
**Justificativa:** Uma classe de produto (`Pizza`) mantém estado detalhado que pertence a outra abstração (`Cliente`), misturando responsabilidades de duas entidades diferentes.

---

## 3. Má Distribuição de Responsabilidades (Divergent Change)
**Onde:** classe `Pizza`
**Justificativa:** Mudanças em regras de negócio de cliente, marketing, fidelidade e reclamações exigiriam alterações todas dentro da mesma classe `Pizza`, indicando que a classe é afetada por diferentes motivos de mudança.

---

## 4. Obsessão por Tipos Primitivos (Primitive Obsession)
**Onde:** atributos e parâmetros como `size`, `dough_type`, `topping` (strings), `customer_phone_number`, `customer_email`, `discount_code`.
**Justificativa:** Conceitos que poderiam ser objetos (ex.: `Tamanho`, `Telefone`, `Email`, `CódigoDesconto`) são representados por tipos primitivos (`str`), sem validação ou comportamento encapsulado.

---

## 5. Lista de Parâmetros Longa (Long Parameter List)
**Onde:** `update_customer_info(self, first_name, last_name, address, phone_number, email)`
**Justificativa:** O método recebe cinco parâmetros relacionados entre si — candidato natural a agrupamento em um objeto, indicando excesso de parâmetros.

---

## 6. Lista de Parâmetros Longa (Long Parameter List)
**Onde:** `order_with_unnecessary_details(self, pizza_type, size, crust_type, toppings, extra_cheese, discount_code)`
**Justificativa:** Seis parâmetros, muitos dos quais nem são usados de fato no corpo do método, caracterizando lista de parâmetros excessiva.

---

## 7. Método Longo (Long Method)
**Onde:** `long_method(self)`
**Justificativa:** O método executa uma sequência extensa de chamadas (configuração de pizza, atualização de cliente, três notificações, descontos, fidelidade, reclamação) misturando muitas responsabilidades em um único bloco.

---

## 8. Método com Nome Revelador de Mau Uso (Long Parameter List / Funções com nomes inadequados)
**Onde:** `another_unused_method`, `yet_another_unused_method`
**Justificativa:** Métodos vazios (`pass`), cujo próprio nome declara seu propósito inexistente.

---

## 9. Código Morto (Dead Code)
**Onde:** `another_unused_method`, `yet_another_unused_method`, `refused_bequest`
**Justificativa:** Métodos que contêm apenas `pass`, sem qualquer funcionalidade — código não utilizado.

---

## 10. Código Duplicado (Duplicated Code)
**Onde:** `duplicate_method(self)`
**Justificativa:** O método chama `self.set_topping("Cheese")` duas vezes consecutivas, repetindo exatamente a mesma instrução.

---

## 11. Código Duplicado (Duplicated Code)
**Onde:** métodos `update_customer_name`, `update_customer_address`, `update_customer_phone_number`, `update_customer_email`
**Justificativa:** Eles repetem a mesma lógica de atribuição já contida em `update_customer_info`, apenas com subconjuntos de parâmetros.

---

## 12. Cadeia de Mensagens (Message Chain / Chain of Methods)
**Onde:** `chain_of_methods(self)`
**Justificativa:** O método indica explicitamente uma cadeia de mensagens/encadeamento de chamadas entre objetos, um acoplamento de "trem de chamadas".

---

## 13. Intermediário (Middle Man)
**Onde:** `middleman_method(self)` e `middle_method(self)`
**Justificativa:** Ambos apenas delegam a chamada para outro método (`middle_method` e `real_method`, respectivamente), sem agregar comportamento próprio.

---

## 14. Método Delegação Excessiva / Classe Intermediária
**Onde:** `middleman_method` → `middle_method` → `real_method`
**Justificativa:** Uma cadeia de delegações puramente repassadas até o método "real", caracterizando intermediários redundantes.

---

## 15. Exposição de Detalhes Internos (Accessing Internal Details / Feature Envy de introspecção)
**Onde:** `access_internal_details(self)`
**Justificativa:** O método acessa e imprime diretamente atributos internos (`self.size`, `self.dough_type`, `self.topping`), expondo estado interno em vez de encapsular comportamento.

---

## 16. Recusa de Legado / Recusa de Herança (Refused Bequest)
**Onde:** subclasses `CheesePizza`, `VeggiePizza`, `TunaPizza`, `PepperoniPizza` e método `refused_bequest`
**Justificativa:** As subclasses apenas definem construtores com valores fixos e não utilizam praticamente nenhum comportamento herdado de `Pizza`; além disso, o próprio método `refused_bequest` está vazio. As subclasses herdam um grande conjunto de métodos que não usam ou não fazem sentido para elas (herança mal aproveitada).

---

## 17. Herança Recusada / Hierarquia Inadequada
**Onde:** `CheesePizza`, `VeggiePizza`, `TunaPizza`, `PepperoniPizza`
**Justificativa:** Cada subclasse existe apenas para passar parâmetros fixos ao construtor da classe base, sem estender comportamento. Isso é uma forma de herança desnecessária, próxima de "Refused Bequest".

---

## 18. Condicional Longa / Switch Statements (Conditional Complexity)
**Onde:** `handle_complaint(self, complaint)` (e a versão sobrescrita em `CheesePizza`)
**Justificativa:** Cadeia de `if/elif/elif/else` sobre o valor de `complaint`, caracterizando lógica condicional ramificada que tende a crescer.

---

## 19. Método com Comportamento Diferente por Herança (Override com `super()`)
**Onde:** `CheesePizza.handle_complaint`
**Justificativa:** Sobrescreve `handle_complaint` adicionando apenas um caso e delegando o resto a `super()`, indicando duplicação parcial de lógica condicional entre classe base e subclasse.

---

## 20. Número Mágico (Magic Number / Magic String)
**Onde:** várias partes — `"cold pizza"`, `"late delivery"`, `"wrong order"`, `"Large"`, `"Thin Crust"`, `"Pepperoni"`, `"Cheese"`, `"123 Street"`, `"555-5555"`, `"john.doe@example.com"`
**Justificativa:** Valores literais repetidos diretamente no código sem constante nomeada, dificultando manutenção e aumentando risco de inconsistência.

---

## 21. Acoplamento a Detalhes de Implementação / Vazamento de Estado (Temporary Field)
**Onde:** `temp_discount_code`, `temp_order_note`
**Justificativa:** Campos cujo nome indica uso temporário e que nunca são utilizados no restante do código — variáveis de instância que só existem em determinadas circunstâncias (nunca, neste caso).

---

## 22. Comentário/Atributo Não Utilizado (Dead Code / Speculative Generality)
**Onde:** `extra_cheese` (atributo inicializado como `False`) e parâmetro `extra_cheese` em `order_with_unnecessary_details`
**Justificativa:** O atributo é definido mas nunca efetivamente consumido para comportamento lógico; o parâmetro é apenas impresso, nunca aplicado, sugerindo generalidade especulativa.

---

## 23. Generalidade Especulativa (Speculative Generality)
**Onde:** métodos `another_unused_method`, `yet_another_unused_method`, `refused_bequest` e atributos `temp_*`
**Justificativa:** Elementos criados "para o futuro" (ou por engano) sem uso atual, aumentando a complexidade sem benefício.

---

## 24. Métodos com Nomes Pobres / Falta de Intenção (Comments / Naming)
**Onde:** `middle_method`, `real_method`, `long_method`, `chain_of_methods`
**Justificativa:** Nomes genéricos que não expressam a real intenção do método, prejudicando legibilidade e manutenção.

---

## 25. Mistura de Níveis de Abstração (Long Method + Divergent Change)
**Onde:** `long_method`
**Justificativa:** O método combina operações de baixo nível (setar atributos) com operações de alto nível (notificar cliente, aplicar desconto), misturando níveis distintos de abstração.

---

## 26. Ausência de Encapsulamento (Public Fields)
**Onde:** todos os atributos de `Pizza` (`self.size`, `self.customer_*`, etc.)
**Justificativa:** Atributos públicos acessíveis e modificáveis diretamente, permitindo `access_internal_details` e `update_customer_*` manipulá-los sem controle, favorecendo acoplamento.

---

## 27. Classe com Múltiplas Instâncias de Responsabilidade de "Cliente" (Schizophrenic Class / Inappropriate Intimacy)
**Onde:** métodos `notify_for_promotion`, `notify_for_discount`, `notify_for_new_arrivals`, `apply_discount`, `apply_loyalty_points`, `handle_complaint`, `ask_for_receipt`
**Justificativa:** Todos esses métodos operam sobre o conceito de "cliente" (notificações, fidelidade, reclamações), mas estão definidos na classe `Pizza`, demonstrando que a classe tem personalidade dividida entre produto e cliente.

---

## 28. Uso de `print` para Comportamento (Delegação a Saída Padrão / Side-effects)
**Onde:** praticamente todos os métodos da classe
**Justificativa:** Métodos de domínio implementam lógica via `print`, tratando efeitos colaterais de apresentação como comportamento principal — sintoma de responsabilidade mal atribuída.

---

### Resumo por categoria

| Categoria | Ocorrências |
|---|---|
| Large Class | `Pizza` |
| Divergent Change | `Pizza` |
| Inappropriate Intimacy | atributos `customer_*` |
| Primitive Obsession | `size`, `dough_type`, `topping`, `phone`, `email`, `discount_code` |
| Long Parameter List | `update_customer_info`, `order_with_unnecessary_details` |
| Long Method | `long_method` |
| Dead Code | `another_unused_method`, `yet_another_unused_method`, `refused_bequest`, `temp_*`, `extra_cheese` |
| Duplicated Code | `duplicate_method`, métodos `update_customer_*` |
| Message Chain | `chain_of_methods` |
| Middle Man | `middleman_method`, `middle_method` |
| Accessing Internal Details | `access_internal_details` |
| Refused Bequest | subclasses `*Pizza` |
| Switch/Conditional | `handle_complaint` |
| Magic Strings/Numbers | diversos literais |
| Speculative Generality | métodos vazios e atributos `temp_*` |
| Naming | `middle_method`, `real_method`, `long_method` |

Essas são as ocorrências efetivamente presentes no código, conforme solicitado — sem propostas de refatoração.