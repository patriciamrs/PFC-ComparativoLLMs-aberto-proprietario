# Análise de Code Smells — Classe `Shop`

Abaixo estão listados os code smells efetivamente presentes no código apresentado, com método/trecho, identificação e justificativa.

---

## 1. Long Method (Método Longo)

**Trecho:** `long_method()` e `order_with_unnecessary_details()`

**Justificativa:** `long_method()` executa 15 chamadas consecutivas de tarefas completamente distintas (atualização de contato, notificações, descontos, tratamento de reclamação, encadeamento de métodos, etc.). `order_with_unnecessary_details()` acumula várias operações não relacionadas em um único bloco. Métodos com muitas responsabilidades e muitas linhas são difíceis de compreender, testar e manter.

---

## 2. Large Class (Classe Grande / God Class)

**Trecho:** classe `Shop`

**Justificativa:** A classe concentra responsabilidades de múltiplos domínios: criação de pizzas (`create_pizza`), gestão de dados pessoais do cliente (`update_contact_info`, `update_name`, `update_address`, `update_phone_number`, `update_email`), notificações (`notify_for_*`), descontos/fidelidade (`apply_*`), atendimento de reclamações (`handle_complaint`) e recebimento de pedidos (`receive_order`). Uma classe que assume responsabilidades tão díspares caracteriza-se como "God Class".

---

## 3. Divergent Change (Mudança Divergente)

**Trecho:** classe `Shop`

**Justificativa:** Vários motivos independentes podem forçar alterações na mesma classe. Mudanças na lógica de contato, na política de descontos, no fluxo de pedidos ou no tratamento de reclamações exigiriam modificações na classe `Shop`. Uma única classe que precisa mudar por razões diferentes e não relacionadas configura Divergent Change.

---

## 4. Shotgun Surgery (Cirurgia de Espingarda)

**Trecho:** métodos `update_contact_info`, `update_name`, `update_address`, `update_phone_number`, `update_email`

**Justificativa:** Uma alteração no modelo de dados do cliente (por exemplo, adicionar ou renomear um campo) exige modificações em múltiplos métodos espalhados (`update_contact_info`, `update_name`, `update_address`, `update_phone_number`, `update_email`). Mudanças simples que exigem edições em vários pontos do código caracterizam Shotgun Surgery.

---

## 5. Duplicated Code (Código Duplicado)

**Trecho:** métodos `update_contact_info`, `update_name`, `update_address`, `update_phone_number`, `update_email`

**Justificativa:** As atribuições `self.first_name = ...`, `self.last_name = ...`, `self.address = ...`, `self.phone_number = ...` e `self.email = ...` repetem-se de forma idêntica em vários métodos. Além disso, `long_method()` e `order_with_unnecessary_details()` repetem as mesmas sequências de chamadas (`update_contact_info(...)`, `apply_discount()`, `apply_loyalty_points()`).

---

## 6. Middle Man (Homem do Meio)

**Trecho:** métodos `middleman_method()` e `middle_method()`

**Justificativa:** `middleman_method()` apenas delega para `middle_method()`, que por sua vez apenas delega para `real_method()`. Esses métodos não agregam comportamento próprio, servindo unicamente como intermediários para repassar chamadas. A própria nomenclatura do código ("middleman/middle") evidencia a intenção.

---

## 7. Message Chains (Cadeia de Mensagens)

**Trecho:** métodos `chain_of_methods()` e `access_internal_details()`

**Justificativa:** `chain_of_methods()` acessa `self.casher.chef.clean_kitchen()` e `access_internal_details()` acessa `self.casher.chef.busy`. Essas navegações em cascata de objetos (`Shop → Cashier → Chef`) criam acoplamento forte com a estrutura interna de outros objetos, caracterizando Message Chains (também conhecida como "train wreck").

---

## 8. Inappropriate Intimacy (Intimidade Inapropriada)

**Trecho:** método `access_internal_details()`

**Justificativa:** O método acessa diretamente o atributo interno `busy` de `self.casher.chef`, expondo e dependendo de detalhes internos de outra classe. O próprio nome do método ("access internal details") explicita a violação do encapsulamento.

---

## 9. Dead Code (Código Morto)

**Trecho:** métodos `another_unused_method()` e `yet_another_unused_method()`

**Justificativa:** Ambos os métodos possuem corpo `pass` e nomes que indicam explicitamente que são "unused" (não utilizados). Não há chamada a eles em nenhum ponto do código, portanto nunca são executados.

---

## 10. Comments (Comentários) — *parcialmente aplicável*

**Observação:** Não há comentários explicativos no corpo do código que justifiquem este smell. Os únicos blocos de texto no topo são o cabeçalho de licença e a nota de pesquisa ("This dataset contains smelly code for research and refactoring purposes"). Por isso, **este smell não é identificado como ocorrência no código funcional** — é apenas mencionado para completude.

---

## 11. Switch Statements (Comandos Switch / Condicionais Encadeadas)

**Trecho:** `create_pizza()` e `handle_complaint()`

**Justificativa:** `create_pizza()` usa uma longa cadeia de `if/elif` para instanciar diferentes tipos de pizza, e `handle_complaint()` usa uma cadeia de `if/elif` para tratar diferentes reclamações. Embora todos os ramos de `handle_complaint()` chamem o mesmo método `calm_customer_down()`, a estrutura de decisão encadeada baseada em tipo/categoria é característica do smell Switch Statements (ausência de polimorfismo para tratar variação de comportamento por tipo).

---

## 12. Speculative Generality (Generalidade Especulativa)

**Trecho:** atributos `frequent_customer_discount`, `temp_discount_code`, `temp_order_note` e métodos `notify_for_promotion`, `notify_for_discount`, `notify_for_new_arrivals`, `apply_discount`, `apply_loyalty_points`, `ask_for_receipt`

**Justificativa:** Vários atributos são inicializados (`None`/`False`) e métodos são criados sem que exista fluxo funcional que realmente os utilize de forma integrada ao domínio. São estruturas criadas para uso futuro/especulativo, sem necessidade concreta demonstrada no código.

---

## 13. Lazy Class (Classe Preguiçosa) — *aplicável aos métodos vazios*

**Trecho:** métodos `another_unused_method()` e `yet_another_unused_method()`

**Justificativa:** Métodos que não realizam nenhum trabalho (corpo `pass`) não justificam sua existência. Estão relacionados ao Dead Code e à classe/membros que não agregam valor suficiente para se manterem.

---

## 14. Temporary Field (Campo Temporário)

**Trecho:** atributos `temp_discount_code` e `temp_order_note`

**Justificativa:** Os nomes ("temp_") indicam que são campos de uso temporário, inicializados como `None` e não utilizados de forma consistente em nenhum método durante a análise do fluxo. Campos que só fazem sentido em determinadas situações temporárias e ficam vazios no restante do tempo caracterizam Temporary Field.

---

## 15. Data Class (Classe de Dados)

**Trecho:** conjunto de atributos `first_name`, `last_name`, `address`, `phone_number`, `email` com seus métodos `update_*`

**Justificativa:** A classe armazena dados do cliente e oferece apenas getters/setters implícitos (métodos de atualização) sem comportamento de domínio significativo associado a esses dados, caracterizando uma estrutura de Data Class embutida na `Shop`.

---

## Resumo consolidado

| # | Code Smell | Local |
|---|-----------|-------|
| 1 | Long Method | `long_method`, `order_with_unnecessary_details` |
| 2 | Large Class / God Class | classe `Shop` |
| 3 | Divergent Change | classe `Shop` |
| 4 | Shotgun Surgery | métodos `update_*` |
| 5 | Duplicated Code | métodos `update_*`, chamadas repetidas |
| 6 | Middle Man | `middleman_method`, `middle_method` |
| 7 | Message Chains | `chain_of_methods`, `access_internal_details` |
| 8 | Inappropriate Intimacy | `access_internal_details` |
| 9 | Dead Code | `another_unused_method`, `yet_another_unused_method` |
| 10 | Switch Statements | `create_pizza`, `handle_complaint` |
| 11 | Speculative Generality | atributos/métodos não utilizados |
| 12 | Temporary Field | `temp_discount_code`, `temp_order_note` |
| 13 | Data Class | atributos de cliente + `update_*` |
| 14 | Lazy Class | métodos vazios |

> **Nota:** Como solicitado, esta análise identifica apenas os smells presentes, sem propor refatorações. Vários métodos (como `long_method`) aparecem repetidamente porque concentram mais de um smell simultaneamente, o que é típico de código de pesquisa de refatoração como o apresentado.