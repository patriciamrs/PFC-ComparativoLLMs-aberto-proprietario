# Análise de Code Smells — Código Pizza (Python)

### 1. Large Class (Classe Grande)
- **Localização:** Classe `Pizza`.
- **Justificativa:** A classe possui muitos atributos e métodos, acumulando responsabilidades relacionadas à configuração de pizzas, informações de clientes, promoções, descontos, reclamações e pedidos. Essa concentração de funcionalidades caracteriza uma classe com responsabilidades excessivas.

### 2. Long Method (Método Longo)
- **Localização:** Método `long_method()`.
- **Justificativa:** O método realiza diversas operações diferentes em sequência, incluindo configuração da pizza, atualização de informações do cliente, notificações promocionais, aplicação de descontos e tratamento de reclamações. A quantidade e a diversidade dessas operações indicam que o método concentra responsabilidades demais.

### 3. Long Parameter List (Lista Longa de Parâmetros)
- **Localização:** Método `order_with_unnecessary_details()`.
- **Justificativa:** O método recebe seis parâmetros (`pizza_type`, `size`, `crust_type`, `toppings`, `extra_cheese` e `discount_code`), tornando sua interface extensa e exigindo o fornecimento de diversas informações em uma única chamada.

### 4. Data Clumps (Agrupamento de Dados)
- **Localização:** Atributos `customer_first_name`, `customer_last_name`, `customer_address`, `customer_phone_number` e `customer_email`, além do método `update_customer_info()`.
- **Justificativa:** As informações relacionadas ao cliente aparecem agrupadas como atributos e como parâmetros de um método. Esses dados representam um conjunto de informações relacionadas que são tratadas conjuntamente.

### 5. Divergent Change (Mudança Divergente)
- **Localização:** Classe `Pizza`.
- **Justificativa:** A classe reúne funcionalidades de diferentes áreas, como preparação de pizzas, gerenciamento de dados de clientes, promoções, descontos e reclamações. Alterações nessas funcionalidades podem exigir modificações na mesma classe por motivos distintos.

### 6. Feature Envy (Inveja de Funcionalidade)
- **Localização:** Métodos `update_customer_info()`, `update_customer_name()`, `update_customer_address()`, `update_customer_phone_number()` e `update_customer_email()`.
- **Justificativa:** Esses métodos manipulam exclusivamente informações relacionadas ao cliente, embora estejam implementados na classe `Pizza`. Isso indica que a classe possui comportamentos mais relacionados à responsabilidade de gerenciamento de clientes do que à representação de uma pizza.

### 7. Duplicate Code (Código Duplicado)
- **Localização:** Método `duplicate_method()`.
- **Trecho identificado:** `self.set_topping("Cheese")`, executado duas vezes consecutivas.
- **Justificativa:** A mesma chamada é executada duas vezes consecutivas, com o mesmo argumento, representando uma duplicação literal de código sem diferença de comportamento entre as operações.

### 8. Middle Man (Intermediário)
- **Localização:** Método `middle_method()`, chamado por `middleman_method()`.
- **Justificativa:** O método atua principalmente como intermediário, encaminhando a execução para `real_method()`, sem acrescentar uma operação significativa relacionada à funcionalidade delegada.

### 9. Speculative Generality (Generalidade Especulativa)
- **Localização:** Métodos `another_unused_method()`, `yet_another_unused_method()` e `refused_bequest()`.
- **Justificativa:** Os métodos possuem apenas a instrução `pass`, sem implementar qualquer comportamento. Sua presença sugere estruturas criadas sem uma necessidade funcional demonstrada no código apresentado.
