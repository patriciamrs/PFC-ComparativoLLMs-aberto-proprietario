# Análise de Code Smells

Abaixo está a identificação dos code smells presentes no código. Observo que o arquivo apresentado contém apenas a classe `main` (ver nota ao final sobre as classes referenciadas).

---

## 1. Nome de classe em minúscula (violação de convenção de nomenclatura / *Naming Convention Violation*)

**Trecho:** Declaração da classe `public class main {`

**Justificativa:** A convenção de nomenclatura Java (e a própria identidade do code smell "código em desacordo com padrões de estilo") exige que nomes de classes sejam escritos em *PascalCase*, iniciando com letra maiúscula. O nome `main` está em minúsculas, o que não apenas viola a convenção como causa confusão com o método `main`, dificultando a leitura e a distinção entre o tipo e o ponto de entrada do programa.

---

## 2. Método com múltiplas responsabilidades dentro da lógica de medição (mistura de responsabilidades / *doing too much* — coesão baixa)

**Trecho:** Método `measureExecutionTime()`, especialmente o bloco do `for`:

```java
Shop shop = new Shop();
Customer customer = new Customer(shop);
customer.orderPizza("Cheese");
customer.complain("The pizza is too cold.");
```

**Justificativa:** O método que deveria apenas medir tempo de execução também é responsável por **definir o cenário de negócio** (criar `Shop`, `Customer`, escolher a pizza "Cheese", escolher a reclamação). Ele acumula responsabilidades de temporização e de configuração do domínio, reduzindo a coesão. Um método coeso deveria ter uma única responsabilidade clara.

---

## 3. Números e *strings* mágicos (*Magic Numbers* e *Magic Strings*)

**Trecho:** Dentro de `measureExecutionTime()`:

- `int runs = 10;`
- `customer.orderPizza("Cheese");`
- `customer.complain("The pizza is too cold.");`
- `// Convert nanoseconds to seconds` com `1_000_000_000.0`

**Justificativa:** Valores literais (`10`, `"Cheese"`, `"The pizza is too cold."`, `1_000_000_000.0`) aparecem embutidos diretamente no código sem nomes explicativos. Isso caracteriza *Magic Numbers* e *Magic Strings*: valores que carregam significado de negócio ou de configuração, mas cuja intenção não é autoexplicativa. Alterar qualquer um deles exige procurar e editar o literal espalhado no código, dificultando manutenção e entendimento.

---

## 4. Uso de tipos primitivos/inseguros para representar conceitos de domínio (*Primitive Obsession* — tendência)

**Trecho:** `int runs = 10;` e o retorno `double` de `measureExecutionTime()`, manipulando tempos em `long`/`double`.

**Justificativa:** O código representa conceitos como "número de execuções" e "tempo de execução" usando tipos primitivos (`int`, `long`, `double`) misturados em diferentes unidades (nanossegundos e segundos), com o comentário `// Convert nanoseconds to seconds` explicitando a fragilidade. Há obsessão por primitivos em vez de abstrações que encapsulem valor + unidade, o que favorece erros de conversão.

---

## 5. Código copiado/estrutura repetida de acumulação (*Duplicated Code* — repetição de padrão de loop)

**Trecho:** Os dois loops em `measureExecutionTime()`:

```java
for (int i = 0; i < runs; i++) { ... executionTimes.add(executionTime); }
...
for (Long time : executionTimes) {
    totalExecutionTime += time;
}
```

**Justificativa:** Há duas estruturas de iteração que fazem tarefas equivalentes de percorrer/acumular valores sobre a coleção de tempos. O segundo laço poderia ser substituído por uma operação de redução/soma, o que evidencia o padrão de duplicação de lógica de agregação em vez de reaproveitar uma operação existente. *(Observação: classifico aqui como duplicação de padrão de iteração — veja a nota abaixo.)*

---

## 6. Comentário compensando código pouco claro (*Comment as a substitute for clarity* / *Obscure Code with Comments*)

**Trecho:** `return totalExecutionTime / runs / 1_000_000_000.0; // Convert nanoseconds to seconds`

**Justificativa:** O comentário existe para explicar *o que* o código faz, e não *por que*. A expressão encadeada de divisões com o literal `1_000_000_000.0` é pouco autoexplicativa; o comentário mascara a falta de clareza sem resolvê-la. Comentários que compensam código obscuro são considerados code smell.

---

## 7. Efeitos colaterais ocultos em código de medição (*Hidden Side Effects* / falta de isolamento)

**Trecho:** O corpo do `for` em `measureExecutionTime()` instancia objetos e executa ações de negócio (`orderPizza`, `complain`) a cada iteração.

**Justificativa:** O método aparenta ser um utilitário de medição de tempo, mas na verdade provoca efeitos colaterais significativos (criação de objetos, alteração de estado de domínio como pedidos e reclamações). Isso torna seu comportamento não óbvio a partir da assinatura, representando um efeito colateral escondido — especialmente problemático num método que se repete 10 vezes, potencialmente acumulando estado.

---

## Nota de escopo

O trecho fornecido contém **apenas** a classe `main`. Não foram incluídas no enunciado as definições de `Shop` e `Customer`. Portanto, smells que dependem da implementação dessas classes (p.ex. *Inappropriate Intimacy* entre `Customer` e `Shop`, *God Class*, *Feature Envy*) **não podem ser confirmados** apenas com este arquivo e por isso não estão listados como ocorrências efetivas. Os smells acima são os que se sustentam com base exclusivamente no código apresentado.

Se você puder enviar também as classes `Shop` e `Customer`, posso complementar a análise com os smells que dependem delas.