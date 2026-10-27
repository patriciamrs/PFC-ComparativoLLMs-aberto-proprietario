# Análise de Code Smells — Classe `Chef`

Abaixo está a identificação de todos os code smells presentes no código apresentado. Note que muitos deles são intencionais no dataset (marcados como "smelly code for research"), e alguns até se auto-referenciam pelos nomes dos métodos.

---

## 1. Classe Grande / Classe Deus (Large Class / God Class)
**Onde:** classe `Chef` como um todo.

**Justificativa:** A classe acumula responsabilidades de domínios completamente distintos: preparo de pizza (culinária), gestão de dados pessoais/contato do cliente, notificações de marketing (promoção, desconto, novidades), aplicação de descontos e pontos de fidelidade, tratamento de reclamações, e ainda mantém atributos de estado de cozinha (`kitchen_clean`) e de cliente (`first_name`, `address`, `email`). Um `Chef` não deveria gerenciar dados de contato do cliente nem campanhas promocionais. A classe apresenta baixa coesão e tende a crescer indefinidamente.

---

## 2. Método Longo (Long Method)
**Onde:** `long_method`

**Justificativa:** O método invoca sequencialmente 12 operações diferentes, aglutinando responsabilidades de preparo, limpeza, contato e marketing em um único bloco. Isso viola o princípio da responsabilidade única em nível de método e dificulta o entendimento e a manutenção.

---

## 3. Lista de Parâmetros Longa (Long Parameter List)
**Onde:** `update_contact_info` e `order_with_unnecessary_details`

**Justificativa:** Ambos recebem muitos parâmetros de uma vez:
- `update_contact_info(self, first_name, last_name, address, phone_number, email)` — 5 parâmetros.
- `order_with_unnecessary_details(self, pizza_type, size, crust_type, toppings, extra_cheese, discount_code)` — 6 parâmetros, inclusive `discount_code`, que não é usado para nada além de impressão.

Listas longas de parâmetros são difíceis de chamar corretamente e são propensas a erros de ordem/omissão.

---

## 4. Obsessão por Tipos Primitivos (Primitive Obsession)
**Onde:** atributos `phone_number`, `email`, `address` e `pizza_type`; métodos `bake_pizza`, `update_*`.

**Justificativa:** Conceitos que têm estrutura e regras próprias (telefone, e-mail, endereço) são representados por `str` cru. Não há validação nem encapsulamento — qualquer string é aceita como e-mail, telefone ou endereço. Isso também é visível em `Pizza(...)` recebendo `"Unknown"` como strings ("size"/"crust").

---

## 5. Código Duplicado (Duplicated Code)
**Onde:** `update_contact_info` versus os métodos `update_name`, `update_address`, `update_phone_number`, `update_email`.

**Justificativa:** Os quatro métodos `update_*` apenas reatribuem individualmente cada atributo que `update_contact_info` já faz em conjunto. A lógica de atribuição está repetida.

---

## 6. Método Duplicado (Duplicated Code / Duplicate Method)
**Onde:** `duplicate_method`

**Justificativa:** O próprio nome e corpo evidenciam o smell: chama `bake_pizza("Cheese")` duas vezes seguidas, sem variar parâmetro. É a representação literal de lógica duplicada.

---

## 7. Código Morto / Métodos Não Utilizados (Dead Code — Unused Methods)
**Onde:** `another_unused_method`, `yet_another_unused_method`, `refused_bequest`

**Justificativa:** São métodos vazios (`pass`) que não são chamados em nenhum lugar. Adicionam ruído à classe sem entregar comportamento.

---

## 8. Método Vazio / Código Vazio sem Propósito (Empty Method)
**Onde:** `middle_method` (delegação sem valor agregado), `real_method`, `refused_bequest`, `another_unused_method`, `yet_another_unused_method` (corpos irrelevantes).

**Justificativa:** Sobretudo `refused_bequest` e os `*_unused_method` são corpos vazios sem função. `middle_method`/`real_method` existem apenas para produzir encadeamento artificial, sem lógica real.

---

## 9. Classe Alternativa por Parâmetros Diferentes / Métodos que Deveriam Ser Estáticos ou Não Usam Estado
**Onde:** `Chef.bake_pizza`, `cut_pizza_and_put_in_box`, `deliver_pizza`, `hurry_up`, `notify_for_promotion`, `notify_for_discount`, `notify_for_new_arrivals`, `apply_discount`, `apply_loyalty_points`, `ask_for_receipt`

**Justificativa:** Vários métodos apenas imprimem mensagens e não manipulam estado da classe ou não usam `self` de forma relevante. Por exemplo, `apply_discount` ignora o `discount_code` recebido em `order_with_unnecessary_details`. Isso é o smell de *métodos que não usam os próprios dados / poderiam ser estáticos*.

---

## 10. Encadeamento de Mensagens (Message Chains)
**Onde:** `middleman_method` → `middle_method` → `real_method`

**Justificativa:** A cadeia `middleman_method` chama `middle_method`, que chama `real_method`. O texto de impressão ("Chef is calling a middleman method", "delegating to another method") confirma a intenção: o cliente depende de uma sequência de delegações para chegar ao trabalho real.

---

## 11. Intermediário / Middleman (Middle Man / Delegation Overuse)
**Onde:** `middleman_method` e `middle_method`

**Justificativa:** `middleman_method` não faz nada além de chamar `middle_method`, que por sua vez não faz nada além de chamar `real_method`. Métodos puramente delegadores adicionam indireção sem agregar valor.

---

## 12. Cadeia de Métodos de Chamada Interna Desnecessária / Encadeamento Interno (em `middle_method`)
**Onde:** `middle_method`

**Justificativa:** Idêntico ao item anterior sob outra ótica: o método só serve de "ponte" entre dois pontos, caracterizando *Middle Man*.

---

## 13. Instinto de Inveja (Feature Envy)
**Onde:** métodos de marketing e cliente dentro de `Chef` (`notify_for_promotion`, `notify_for_discount`, `notify_for_new_arrivals`, `apply_discount`, `apply_loyalty_points`, `ask_for_receipt`, `update_contact_info`, `update_*`, `handle_complaint`).

**Justificativa:** Essas operações manipulam, na essência, o domínio do **cliente** (contato, promoções, pontos, reclamações) e não o domínio do **chef**. Uma classe `Chef` que fala em "Customer is asking for a receipt" ou "Applying loyalty points for customer" demonstra inveja das responsabilidades de uma classe de cliente (`Customer`).

---

## 14. Estrutura Condicional Excessiva (Switch/Conditional Statements — "if-else" chain)
**Onde:** `handle_complaint`

**Justificativa:** O método faz uma cascata de `if/elif/elif/else` sobre o tipo de reclamação — mas **todos os ramos executam exatamente a mesma ação** (`self.clean_kitchen()`). É um condicional extenso e inútil, que seria substituído por uma única chamada — sintoma clássico de *Switch Statements* e de lógica degenerada.

---

## 15. Estrutura Condicional Redundante / Condicional Sem Efeito (Redundant Conditional)
**Onde:** `handle_complaint`

**Justificativa:** Reforçando o item 13: cada ramo é idêntico, ou seja, o custo de manutenção do condicional é puro desperdício. Caracteriza smell de complexidade condicional inflada sem valor.

---

## 16. Números Mágicos / Strings Mágicas (Magic Numbers/Strings)
**Onde:** `bake_pizza("Cheese")`, `handle_complaint("cold pizza")`, `Pizza("Unknown", "Unknown", pizza_type)`

**Justificativa:** Literais de string com significado semântico ("Cheese", "cold pizza", "Unknown") aparecem espalhados pelo código sem constante nomeada. Repetem-se em `bake_pizza`, `long_method` e `duplicate_method`, aumentando a chance de erro quando o valor mudar.

---

## 17. Atributos Temporários / Campos Desnecessários (Temporary Field)
**Onde:** `temp_discount_code`, `temp_order_note`, além de vários atributos nunca usados.

**Justificativa:** `temp_discount_code` e `temp_order_note` são inicializados como `None` e **nunca são usados em nenhum método**. Pelo nome ("temp_"), indicam campos que só seriam relevantes em contextos específicos — o cheiro de *Temporary Field* (campos cujo significado depende de um estado incomum da classe).

---

## 18. Atributos Não Utilizados (Unused Fields / Dead Attributes)
**Onde:** `completed_orders`, `breaks_taken`, `frequent_customer_discount`, `temp_discount_code`, `temp_order_note`, e boa parte de `first_name/last_name/address/phone_number/email` fora de `update_*`.

**Justificativa:** Vários desses atributos são declarados e inicializados, mas nunca lidos para lógica de decisão. Ex.: `completed_orders` e `breaks_taken` nunca são incrementados nem verificados; `frequent_customer_discount` nunca é consultado. São estados mortos que inchaço a classe.

---

## 19. Flag de Estado Manipulada Trivialmente (Boolean/Flag Smell)
**Onde:** `self.kitchen_clean`, `self.busy`, `self.frequent_customer_discount`

**Justificativa:** `busy` nunca é alterado; `kitchen_clean` só é setado para `True` por `clean_kitchen` e nunca lido para decisão; `frequent_customer_discount` nunca é alterado. Flags booleanas sem uso real caracterizam *Flag Arguments / Boolean Blindness* de estado, sinalizando lógica inacabada.

---

## 20. Comentários Inúteis / Ruído de Números Mágicos de Impressão

## 21. Interface Não Utilizada (Refused Bequest — Interface/Contrato recusado)
**Onde:** `refused_bequest` (por nome) e o design geral da classe.

**Justificativa:** O dataset deixa explícito com o método `refused_bequest` — método existente para herdar/implementar um contrato mas cujo corpo é vazio (`pass`), "recusando" o legado. É o modelo didático do smell *Refused Bequest*. (No código, ele é a representação direta; a herança implícita de `object` é o contrato "recusado".)

---

## 22. Complexidade Desnecessária / Código Especulativo (Speculative Generality)
**Onde:** `another_unused_method`, `yet_another_unused_method`, `middleman_method`, `middle_method`, `real_method`, `chain_of_methods`, `access_internal_details`

**Justificativa:** Estruturas criadas para atender usos especulativos que nunca se materializam — métodos "reservados" (`*_unused_method`), cadeias de delegação, e `access_internal_details` que apenas imprime `self.pizza`. Código especulativo é código que não entrega valor presente.

---

## 23. Exposição de Estado Interno / Violação de Encapsulamento (Access Internal Details)
**Onde:** `access_internal_details`

**Justificativa:** O método expõe detalhes internos via `print(f"Accessing internal details: {self.pizza}")`. O nome confirma: há acesso direto a detalhes internos que deveriam estar encapsulados. Este é o smell *Inappropriate Intimacy / Accessing Internal Details*.

---

## 24. Relacionamento Inapropriado / Intimidade Inadequada (Inappropriate Intimacy)
**Onde:** `bake_pizza` com `Pizza("Unknown", "Unknown", pizza_type)`, `cut_pizza_and_put_in_box` com `self.pizza.topping`.

**Justificativa:** `Chef` acessa diretamente o atributo interno `topping` do objeto `Pizza` e o constrói com valores arbitrários (`"Unknown"`). A classe passa a depender de detalhes de representação de `Pizza`, criando acoplamento excessivo entre as classes.

---

## 25. Acoplamento de Construtor com Valores Placeholder / Construtor com Strings Mágicas
**Onde:** `bake_pizza` → `Pizza("Unknown", "Unknown", pizza_type)`

**Justificativa:** Ao instanciar `Pizza` com `"Unknown"` para tamanho e massa, o código cria objetos em estado possivelmente inválido. É um sintoma de *Primitive Obsession* combinado com *Incomplete Object / placeholder*.

---

## 26. Método que Faz Só Encadeamento de Chamadas Mútuas (Command Chain / Mover com dependência cíclica)
**Onde:** `bake_pizza` → `cut_pizza_and_put_in_box` → `deliver_pizza`

**Justificativa:** `bake_pizza` chama `cut_pizza_and_put_in_box`, que chama `deliver_pizza`. Há uma dependência de chamadas encadeadas que dificulta testar `bake_pizza` isoladamente (`cut_pizza_and_put_in_box` assume que `self.pizza` já existe — acoplamento temporal). Isso evidencia *Temporal Coupling*.

---

## 27. Acoplamento Temporal (Temporal Coupling)
**Onde:** `bake_pizza` e `cut_pizza_and_put_in_box`

**Justificativa:** `cut_pizza_and_put_in_box` só funciona corretamente se `bake_pizza` tiver rodado antes para popular `self.pizza`. Se chamado independentemente, lança `AttributeError` ao acessar `self.pizza.topping`. Dependência de ordem de execução não declarada = *Temporal Coupling*.

---

## 28. Método com Nome Inadequado / Método que Faz Mais de uma Coisa (Método faz coisas demais)
**Onde:** `cut_pizza_and_put_in_box` (corta E embala E entrega), `long_method`

**Justificativa:** `cut_pizza_and_put_in_box` na verdade também chama `deliver_pizza`, ou seja, seu nome esconde uma terceira responsabilidade. Violação do princípio de que a assinatura deve expressar o comportamento — cheiro de *Método que faz múltiplas coisas / Inconsistent Naming*.

---

## 29. Parâmetros Não Utilizados (Unused Parameters)
**Onde:** `order_with_unnecessary_details` → `discount_code` (em `self.apply_discount(discount_code)`, mas `apply_discount` não aceita esse parâmetro — na verdade o método `apply_discount` não tem parâmetros, contradizendo a chamada).

**Justificativa:** O método é chamado como `self.apply_discount(discount_code)`, mas a definição `def apply_discount(self)` não recebe argumento. Isso caracteriza um parâmetro "esquecido"/ignorado na definição — *Unused Parameter* na assinatura que deveria consumir o `discount_code`, e um provável bug latente por assinatura inconsistente.

---

## 30. Interface/Assinatura Inconsistente (Inconsistent Method Signature / Possible Bug Smell)
**Onde:** `order_with_unnecessary_details` chamando `self.apply_discount(discount_code)` vs. `def apply_discount(self)`.

**Justificativa:** Há mismatch entre a chamada e a definição do método — `apply_discount` é chamado com um argumento que não existe na assinatura. É o cheiro de inconsistência entre as partes acopladas, indicando código quebrado/não testado.

---

## 31. Nome de Classe/Método Sugere o Smell (Declarative Smell / Nomes Auto-referenciais)
**Onde:** `long_method`, `duplicate_method`, `middleman_method`, `refused_bequest`, `another_unused_method`, `yet_another_unused_method`, `order_with_unnecessary_details`, `access_internal_details`

**Justificativa:** Os próprios nomes de métodos declaram o smell que representam (por serem didáticos). Isso por si só já é um indício de *má nomenclatura* e serve como documentação do code smell, mas também caracteriza o uso de *nomes que não descrevem comportamento real de negócio*.

---

## 32. Feature Envy / Inveja de Funcionalidade (consolidado em métodos de cliente)
**Onde:** `ask_for_receipt`

**Justificativa:** O método `ask_for_receipt` diz "**Customer** is asking for a receipt", sendo executado dentro de `Chef`. Um método cujo comportamento pertence a outra classe (`Customer`) é o exemplo canônico de *Feature Envy*.

---

## 33. Método com Responsabilidade Fora de Escopo (Divergent Change / Inappropriate Method Placement)
**Onde:** `handle_complaint` e `ask_for_receipt`

**Justificativa:** Chef tratando reclamação de cliente e "pedindo recibo" misturam domínios. A classe tende a mudar por motivos muito diferentes (culinária, atendimento, marketing), caracterizando *Divergent Change*.

---

## 34. Código Duplicado entre Métodos de Impressão (Notificações Duplicadas)
**Onde:** `notify_for_promotion`, `notify_for_discount`, `notify_for_new_arrivals`

**Justificativa:** Três métodos com estrutura idêntica (`print("Notifying customer for X")`), apenas variando o texto. Poderiam ser parametrizados. É duplicação estrutural (*Duplicated Code*).

---

## 35. Ausência de Exceções / Tratamento de Erros (Error Hiding)
**Onde:** `handle_complaint` (o `else` silenciosamente ignora reclamações desconhecidas limpando a cozinha)

**Justificativa:** Reclamações desconhecidas não geram tratamento específico nem erro — todas caem em `clean_kitchen()`. Isso esconde condições inesperadas, um cheiro de lógica que mascara erros (*Error Hiding / Incomplete Logic*).

---

## 36. Injeção de Dependência Hard-Coded / Acoplamento a Classe Concreta
**Onde:** `from Pizza import Pizza` usado diretamente em `bake_pizza`.

**Justificativa:** A classe instancia `Pizza` diretamente (`self.pizza = Pizza(...)`), acoplando-se a uma implementação concreta e dificultando substituição/teste. É *Hard-Coded Dependency / Coupling*.

---

## 37. State Oversight / Estado Não Gerenciado
**Onde:** `self.pizza`, `self.busy`, `kitchen_clean`

**Justificativa:** O campo `self.pizza` é sobrescrito a cada `bake_pizza` e usado implicitamente por `cut_pizza_and_put_in_box`; `busy` nunca alterna. A classe mantém estado que não controla de forma consistente, gerando acoplamento temporal e comportamento imprevisível.

---

## 38. Método "Chain of Methods" Sem Necessidade
**Onde:** `chain_of_methods`

**Justificativa:** O método apenas chama `clean_kitchen()` e imprime uma mensagem sobre "message chain". É um método criado artificialmente sem responsabilidade de negócio, evidenciando *Código Especulativo / Método Vazio de sentido*.

---

## 39. Número Excessivo de Atributos (Many Fields / Data Class)
**Onde:** `__init__` da classe `Chef` (14 atributos).

**Justificativa:** A classe mantém 14 campos heterogêneos (estado de cozinha, dados do cliente, contadores, flags de desconto, campos temporários). Alta densidade de atributos com pouca coesão é sintoma de *Data Class / Large Class* — aqui, manual de "classe que só acumula dados".

---

# Resumo das Categorias de Smells Identificadas

| # | Code Smell | Local |
|---|-----------|-------|
| 1 | Large Class / God Class | `Chef` |
| 2 | Long Method | `long_method` |
| 3 | Long Parameter List | `update_contact_info`, `order_with_unnecessary_details` |
| 4 | Primitive Obsession | `phone_number`, `email`, `address`, `pizza_type` |
| 5 | Duplicated Code | `update_*` vs `update_contact_info`; `notify_*` |
| 6 | Duplicate Method | `duplicate_method` |
| 7 | Dead Code / Unused Method | `another_unused_method`, `yet_another_unused_method` |
| 8 | Empty Method | `refused_bequest`, `middle_method`, `real_method` |
| 9 | Método que não usa estado / poderia ser estático | métodos de `print` |
| 10 | Message Chains | `middleman_method → middle_method → real_method` |
| 11 | Middle Man | `middleman_method`, `middle_method` |
| 12 | Feature Envy | `ask_for_receipt`, `apply_*`, `notify_*`, `update_*` |
| 13 | Switch/Conditional Statements | `handle_complaint` |
| 14 | Redundant Conditional | `handle_complaint` |
| 15 | Magic Strings/Numbers | `"Cheese"`, `"cold pizza"`, `"Unknown"` |
| 16 | Temporary Field | `temp_discount_code`, `temp_order_note` |
| 17 | Unused Fields | `completed_orders`, `breaks_taken`, `frequent_customer_discount`, etc. |
| 18 | Flag Smell (Boolean) | `busy`, `kitchen_clean`, `frequent_customer_discount` |
| 19 | Refused Bequest | `refused_bequest` |
| 20 | Speculative Generality | `chain_of_methods`, `access_internal_details`, `*_unused_method` |
| 21 | Inappropriate Intimacy | acesso a `self.pizza.topping` |
| 22 | Temporal Coupling | `bake_pizza` ↔ `cut_pizza_and_put_in_box` |
| 23 | Unused Parameter | `discount_code` em `order_with_unnecessary_details` |
| 24 | Assinatura Inconsistente (Bug Smell) | `apply_discount(discount_code)` vs `def apply_discount(self)` |
| 25 | Divergent Change | `Chef` (culinária + atendimento + marketing) |
| 26 | Error Hiding | `else` de `handle_complaint` |
| 27 | Hard-Coded Dependency | `Pizza("Unknown", ...)` |
| 28 | Data Class / Many Fields | `__init__` com 14 atributos |
| 29 | Inconsistent Naming | `cut_pizza_and_put_in_box` (também entrega) |

---

**Observação final:** o código é um exemplo deliberado de "smelly code" (conforme o cabeçalho do arquivo declara: *"This dataset contains smelly code for research and refactoring purposes"*), e vários métodos têm nomes que auto-declaram o smell que representam (ex.: `long_method`, `duplicate_method`, `middleman_method`, `refused_bequest`). Não foram propostas refatorações, conforme solicitado.