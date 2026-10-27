# Análise de Code Smells — Classe `Customer`

Abaixo estão os code smells identificados no código apresentado, organizados por tipo. Nenhuma alteração ou refatoração é proposta, conforme solicitado.

---

## 1. Código Morto (Dead Code) / Métodos Não Utilizados

**Onde ocorre:**

- Métodos `another_unused_method()` e `yet_another_unused_method()`
- Métodos `handle_complaint(complaint)`, `apply_discount()`, `apply_loyalty_points()`, `notify_for_promotion()`, `notify_for_discount()`, `notify_for_new_arrivals()`, `refused_bequest()`, `update_contact_info()`, `update_name()`, `update_address()`, `update_phone_number()`, `update_email()`

**Justificativa:** Os métodos `another_unused_method` e `yet_another_unused_method` têm corpo vazio (`pass`) e nomes que explicitamente indicam que não são usados. Além disso, diversos métodos (`handle_complaint`, `apply_discount`, `notify_*`, `refused_bequest`, etc.) não são chamados em nenhum ponto da própria classe, indicando código que provavelmente nunca é executado. O nome `refused_bequest` (grafia incorreta de *refused bequest*) é, ele próprio, uma pista de que se trata de código morto intencional para fins de pesquisa.

---

## 2. Método Longo (Long Method)

**Onde ocorre:**

- `long_complaint_method()`
- `order_with_unnecessary_details()`
- `duplicate_complaint()`

**Justificativa:** Esses métodos acumulam muitas instruções sequenciais em um único corpo. `long_complaint_method` executa seis chamadas consecutivas de `complain(...)` seguidas de `ask_for_receipt`. `order_with_unnecessary_details` realiza uma única chamada com **vinte argumentos**, tornando o método extenso e de difícil leitura. `duplicate_complaint` repete quatro chamadas em sequência. Nessas construções o método concentra múltiplas responsabilidades e cresce em linhas, caracterizando método longo.

---

## 3. Lista de Parâmetros Longa (Long Parameter List)

**Onde ocorre:**

- `order_with_unnecessary_details()` → chamada `self.order_pizza("Veggie", "Large", "Whole Wheat", "Veggies", False, True, False, False, "Olives", "Mushrooms", "Pesto", "Thick", False, False, True, True, True, False, False, False)`
- `update_contact_info(self, first_name, last_name, address, phone_number, email)`

**Justificativa:** A chamada de `order_pizza` passa 20 argumentos (a maioria booleanos sem significado evidente), e `update_contact_info` recebe 5 parâmetros de uma vez. Listas de parâmetros extensas dificultam a compreensão da chamada, aumentam a chance de erro de ordem dos argumentos e indicam que os dados deveriam estar agrupados em um objeto.

---

## 4. Obsessão por Tipos Primitivos (Primitive Obsession)

**Onde ocorre:**

- Atributos `self.first_name`, `self.last_name`, `self.address`, `self.phone_number`, `self.email` (em `__init__` e nos métodos `update_*`)

**Justificativa:** Dados que formam um conceito coeso — os dados de contato/nome de um cliente — são representados como uma coleção de campos primitivos (`str`/`None`) espalhados pela classe, em vez de um objeto de domínio (ex.: uma classe `ContactInfo` ou `CustomerName`). O mesmo padrão aparece na chamada de `order_pizza`, em que a preferência de pizza é expressa por uma longa sequência de `strings` e `booleans` primitivos.

---

## 5. Números Mágicos / Booleanos Mágicos (Magic Numbers / Magic Booleans)

**Onde ocorre:**

- Chamada em `order_with_unnecessary_details()`: `... False, True, False, False, ..., True, True, True, False, False, False`

**Justificativa:** A sequência de valores booleanos literais (`True`/`False`) não possui nome nem contexto, obrigando o leitor a adivinhar o que cada posição representa. São "valores mágicos" porque seu significado só é conhecido pela posição na assinatura do método.

---

## 6. Cadeia de Mensagens (Message Chains)

**Onde ocorre:**

- `complain()`: `self.pizza_shop.casher.chef.clean_kitchen()`
- `chain_of_methods()`: `self.pizza_shop.casher.chef.clean_kitchen()`
- `access_internal_details()`: `self.pizza_shop.casher.chef.busy`

**Justificativa:** O cliente navega por uma cadeia de objetos (`pizza_shop → casher → chef`) para acessar um comportamento/atributo distante. Isso acopla a classe `Customer` à estrutura interna de navegação de outras classes; qualquer mudança na cadeia quebra o cliente.

---

## 7. Intimidade Inapropriada (Inappropriate Intimacy)

**Onde ocorre:**

- `access_internal_details()`: leitura direta de `self.pizza_shop.casher.chef.busy`
- `complain()` e `chain_of_methods()`: acesso direto a `casher.chef`

**Justificativa:** A classe `Customer` conhece e manipula detalhes internos de outras classes (`PizzaShop`, `casher`, `chef`), inclusive o atributo de estado `busy`. Essa exposição excessiva entre classes caracteriza intimidade inapropriada, em que uma classe depende da implementação interna de outra.

---

## 8. Método Middle Man / Delegacão em Cadeia (Middle Man)

**Onde ocorre:**

- `middleman_method()` → chama `middle_method()` → chama `real_method()`
- `middle_method()`

**Justificativa:** `middleman_method` apenas repassa a chamada para `middle_method`, que por sua vez apenas delega a `real_method`. Os métodos intermediários não adicionam comportamento, funcionando somente como "intermediários" que encaminham a chamada.

---

## 9. Código Duplicado (Duplicated Code)

**Onde ocorre:**

- `duplicate_complaint()`: `self.complain("Pizza is cold")` repetido duas vezes e `self.complain("Pizza is late")` repetido duas vezes
- `complain()` e `chain_of_methods()`: ambos contêm exatamente a mesma chamada `self.pizza_shop.casher.chef.clean_kitchen()`
- Estrutura repetida entre `long_complaint_method()` e `duplicate_complaint()`

**Justificativa:** Há blocos de código idênticos ou quase idênticos repetidos em diferentes pontos da classe. As chamadas duplicadas em `duplicate_complaint` inclusive geram o mesmo efeito; a duplicação de `clean_kitchen()` em dois métodos é redundância de lógica.

---

## 10. Classe Grande / Classe com Baixa Coesão (Large Class / Low Cohesion)

**Onde ocorre:**

- Toda a classe `Customer`

**Justificativa:** A classe reúne responsabilidades muito distintas: fazer pedidos (`order_pizza`, `order_drink`), tratar reclamações (`complain`, `handle_complaint`, `long_complaint_method`), manter dados cadastrais (`update_name`, `update_address`, etc.), emitir notificações (`notify_for_*`), aplicar benefícios (`apply_discount`, `apply_loyalty_points`) e acessar o interior de `PizzaShop`. A ausência de um único foco coeso indica uma classe grande com muitas atribuições.

---

## 11. Declaração de Interruptor / Muitos `if-elif` (Switch Statements / Conditional Complexity)

**Onde ocorre:**

- `handle_complaint(complaint)`

**Justificativa:** O método consiste em uma cadeia `if / elif / elif / else` que ramifica o comportamento de acordo com o valor de `complaint`. Essa estrutura condicional encadeada é o equivalente típico de um `switch` (ou *switch statement*) com muitas ramificações.

---

## 12. Nomes de Métodos/Classe sem Significado ou Enganosos (Mysterious Name / Poor Naming)

**Onde ocorre:**

- `another_unused_method()`, `yet_another_unused_method()`, `middle_method()`, `real_method()`, `refused_bequest()`

**Justificativa:** Os nomes não comunicam a intenção do método. `another_unused_method` / `yet_another_unused_method` não descrevem comportamento; `middle_method` e `real_method` são genéricos; `refused_bequest` descreve um smell, não uma ação. Nomes assim dificultam o entendimento e o uso correto da API da classe.

---

## 13. Abuso de Encapsulamento / Atributos Públicos Expostos

**Onde ocorre:**

- Atributos de instância definidos diretamente e acessados por cadeias externas: `self.frequent_customer_discount`, `self.temp_discount_code`, `self.temp_order_note`, além do acesso `pizza_shop.casher.chef.busy`

**Justificativa:** Os campos são públicos e livres (não encapsulados), e alguns (como `temp_discount_code` e `temp_order_note`) aparentam ser valores temporários/transitórios mantidos como estado de objeto. A combinação de exposição direta e ausência de encapsulamento contribui para o acoplamento e para a fragilidade da classe, reforçando os problemas já citados de intimidade inapropriada.

---

### Observação final

Vários desses itens são sobrepostos por natureza — por exemplo, a cadeia `pizza_shop.casher.chef` configura simultaneamente **Message Chains** e **Inappropriate Intimacy**, e os métodos `update_*` contribuem tanto para **Primitive Obsession** quanto para a **Large Class**. Isso é esperado: em código com muitos smells, os problemas se reforçam mutuamente.

Caso deseje, posso organizar todos esses achados em uma **tabela** (nome do smell × localização × justificativa) ou em um **diagrama** para uso em relatório, mas, conforme pedido, não incluí nenhuma sugestão de refatoração.