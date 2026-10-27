# Análise de Code Smells — Classe `Cashier`

Abaixo estão todos os code smells identificados no código apresentado.

---

## 1. Classe Grande (Large Class — "God Class")

**Onde ocorre:** Toda a classe `Cashier`.

**Justificativa:** A classe acumula responsabilidades muito heterogêneas e sem coesão: atendimento de pedidos, gerenciamento de dados de contato (`first_name`, `last_name`, `address`, `phone_number`, `email`), notificações promocionais, aplicação de descontos, tratamento de reclamações e manipulação do chef. Além disso, mistura dados de **cliente** (contato, promoções, fidelidade) com comportamento de **funcionário/caixa**. A classe possui muitos atributos e muitos métodos, ultrapassando o princípio de responsabilidade única.

---

## 2. Método Longo (Long Method)

**Onde ocorre:** `long_method()`.

**Justificativa:** O método concentra múltiplas tarefas (`take_order`, `hurry_up_chef`, `calm_customer_down`, `deliver_pizza_to_customer`, `ask_for_receipt`) numa única unidade, indicado pelo próprio nome e pela mensagem "handling many tasks in a single method". Deveria ser decomposto em operações menores.

---

## 3. Lista de Parâmetros Longa (Long Parameter List)

**Onde ocorre:** `order_with_unnecessary_details(self, pizza_type, size, crust_type, toppings, extra_cheese, discount_code)` e `update_contact_info(self, first_name, last_name, address, phone_number, email)`.

**Justificativa:** Ambos os métodos recebem muitos parâmetros, dificultando a leitura e o uso. No caso de `update_contact_info`, os parâmetros formam um agrupamento coeso (dados de contato) que poderia ser um objeto único — o que caracteriza também *Data Clump*.

---

## 4. Código Duplicado (Duplicated Code)

**Onde ocorre:** `duplicate_method()` — e de forma correlata nos vários métodos `update_*`.

**Justificativa:** `duplicate_method()` chama `self.take_order("Cheese")` duas vezes seguidas, replicando a mesma operação. Além disso, `update_contact_info`, `update_name`, `update_address` e `update_phone_number`/`update_email` repetem a mesma lógica de atribuição, caracterizando duplicação de código.

---

## 5. Método Morto / Código Não Utilizado (Dead Code / Lazy Class / Unused Method)

**Onde ocorre:** `another_unused_method()`, `yet_another_unused_method()`, `refused_bequest()`.

**Justificativa:** Os três métodos contêm apenas `pass` e nunca são chamados, indicando código morto/não utilizado que introduz ruído sem agregar comportamento.

---

## 6. Número Mágico (Magic Number) / Literais Strings Repetidas

**Onde ocorre:** Diversos métodos com valores literais repetidos, como `"Cheese"` em `long_method()`, `duplicate_method()` e `take_order`; e `200`—decorre de literais em `handle_complaint()` (`"cold pizza"`, `"late delivery"`, `"wrong order"`).

**Justificativa:** Valores como `"Cheese"` e as strings de reclamação aparecem repetidos "hard-coded" sem constante nomeada, tornando o código frágil a mudanças — caracterizando *Magic Strings*/*Magic Numbers*. *(Observação: o código não contém um número inteiro literal de fato, mas a repetição de literais string se enquadra na mesma categoria.)*

---

## 7. Inveja de Dados / Intimidade Inapropriada (Feature Envy / Inappropriate Intimacy)

**Onde ocorre:** `chain_of_methods()` e `access_internal_details()` (`self.chef.busy`).

**Justificativa:** A classe `Cashier` acessa repetidamente membros internos de `Chef` diretamente (`self.chef.busy`, `self.chef.clean_kitchen()`), invadindo a intimidade de outra classe em vez de delegar responsabilidade. `chain_of_methods()` também demonstra encadeamento de mensagens que revela forte acoplamento.

---

## 8. Cadeia de Mensagens (Message Chains)

**Onde ocorre:** `chain_of_methods()`.

**Justificativa:** O método é explicitamente descrito como "initiating a message chain" e encadeia chamadas sobre o objeto `self.chef`, criando uma dependência de navegação entre objetos que torna o código sensível a mudanças na estrutura de colaboração.

---

## 9. Membro Intermediário (Middle Man)

**Onde ocorre:** `middleman_method()` → `middle_method()` → `real_method()`.

**Justificativa:** Os métodos apenas delegam a chamada para o próximo, sem adicionar comportamento próprio, caracterizando o papel de intermediário superfluo apontado pelos nomes e pelas mensagens ("Middleman method delegating to another method").

---

## 10. Classe Preguiçosa / Classe de Dados (Lazy Class / Data Class)

**Onde ocorre:** Atributos e métodos de dados do cliente (`first_name`, `last_name`, `address`, `phone_number`, `email`, `temp_discount_code`, `temp_order_note`, `frequent_customer_discount`).

**Justificativa:** Há um conjunto de atributos com *getters/setters* implícitos (via `update_*`) que armazenam apenas dados do cliente, sem comportamento associado — indicando uma *Data Class* embutida dentro de `Cashier`.

---

## 11. Declarações Switch Repetidas / Condicional Redundante (Repeated Switch / Redundant Condition)

**Onde ocorre:** `handle_complaint()`.

**Justificativa:** O `if/elif/else` possui ramificações diferentes para cada `complaint`, mas **todas executam exatamente a mesma ação** (`self.calm_customer_down()`). A estrutura condicional é redundante, caracterizando um *switch* repetido sem variação de comportamento.

---

## 12. Campo Temporário (Temporary Field)

**Onde ocorre:** `temp_discount_code`, `temp_order_note`.

**Justificativa:** Atributos que só fazem sentido em contextos específicos (e cujos nomes indicam uso temporário) ficam inicializados para `None` no construtor, sendo úteis apenas esporadicamente — definição clássica de *Temporary Field*.

---

## 13. Funcionário/Obsessão Primária por Dados (Primitive Obsession)

**Onde ocorre:** Parâmetros e atributos do tipo string para representar conceitos de domínio: `pizza_type`, `size`, `crust_type`, `toppings`, `phone_number`, `email`, `address`.

**Justificativa:** Conceitos do domínio (tipo de pizza, tamanho, endereço, e-mail, telefone) são representados por primitivas genéricas (`str`) em vez de tipos dedicados, o que caracteriza *Primitive Obsession* — reforçado pela *Long Parameter List* de `order_with_unnecessary_details`.

---

## 14. Nomeação Pobre / do Método com Propósito Implícito (Problematic Naming / Comentário como Nome)

**Onde ocorre:** `order_with_unnecessary_details`, `another_unused_method`, `yet_another_unused_method`, `refused_bequest` (grafia de "bequest"/"request" ambígua).

**Justificativa:** Os nomes descrevem a ausência de propósito ou a presença de defeito em vez de comunicar o comportamento do método, reduzindo a legibilidade e indicando código mantido apenas "para pesquisa".

---

## Resumo

| # | Code Smell | Local |
|---|-----------|-------|
| 1 | Large Class (God Class) | classe `Cashier` inteira |
| 2 | Long Method | `long_method()` |
| 3 | Long Parameter List | `order_with_unnecessary_details()`, `update_contact_info()` |
| 4 | Duplicated Code | `duplicate_method()`, métodos `update_*` |
| 5 | Dead Code / Unused Method | `another_unused_method()`, `yet_another_unused_method()`, `refused_bequest()` |
| 6 | Magic Strings | `"Cheese"`, strings em `handle_complaint()` |
| 7 | Feature Envy / Inappropriate Intimacy | `chain_of_methods()`, `access_internal_details()` |
| 8 | Message Chains | `chain_of_methods()` |
| 9 | Middle Man | `middleman_method()`, `middle_method()` |
| 10 | Data Class / Lazy Class | atributos de contato do cliente |
| 11 | Repeated/Redundant Switch-Conditional | `handle_complaint()` |
| 12 | Temporary Field | `temp_discount_code`, `temp_order_note` |
| 13 | Primitive Obsession | parâmetros `pizza_type`, `size`, `address`, etc. |
| 14 | Naming Problemático | métodos com nomes descritivos de defeito |

> Como solicitado, não foram propostas refatorações — apenas a identificação e justificativa dos code smells efetivamente presentes no código.