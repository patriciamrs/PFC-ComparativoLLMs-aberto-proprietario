# Análise de Code Smells

Antes de apontar os smells, é importante uma observação metodológica: você apresentou apenas o arquivo `main.py`. Os trechos que efetivamente concentram problemas de design (as classes `Shop` e `Customer`) não estão visíveis no código fornecido. Ainda assim, é possível identificar smells no arquivo apresentado — e há um detalhe relevante sobre a estrutura do campo textual.

## Observação sobre o enunciado

O código fornecido aparece dentro de um bloco delimitado por `"""` (três aspas duplas). Em Python, isso constitui uma **docstring/string literal multilinha** atribuída a nenhuma variável, e não código executável. Isso, por si só, é uma anomalia estrutural, mas tratarei os smells considerando o **conteúdo lógico** do código que está dentro dessa string.

---

## Code Smells identificados

### 1. Código Morto (Dead Code) / Código Comentado ou Inacessível

**Onde:** Todo o conteúdo entre `"""` e `"""` (incluindo imports e funções).

**Justificativa:** Todo o código apresentado está enclausurado dentro de um literal de string multilinha. Como string, ele nunca é importado, executado ou avaliado pelo interpretador. Funcionalmente, é equivalente a comentário/código morto: não há caminho de execução que o alcance. Isso é agravado pelo fato de que os imports (`from Shop import Shop`, `from Customer import Customer`) e a função `measure_execution_time` aparecem textualmente como se fossem executáveis, mas não são.

---

### 2. Comentário de Licença/Atribuição Acoplado ao Código (não é smell de código, mas registro)

**Onde:** Bloco inicial `Copyright (c) 2025 Ahmed R. Sadik...`

**Justificativa:** Não é um code smell clássico — é um cabeçalho legal necessário. Registro apenas para delimitar o que é código real: na leitura do arquivo, o `"""` de abertura faz com que o cabeçalho, os imports e a função formem um único literal de string, e não código.

---

### 3. Números Mágicos (Magic Numbers)

**Onde:** `def measure_execution_time(runs=10):`

**Justificativa:** O valor `10` é um literal numérico embutido diretamente como valor padrão do parâmetro, sem nome simbólico que explique o significado (número de execuções para medição). Um leitor precisa inferir o propósito. O mesmo padrão aparece em `average_time = total_time / runs`, herdando a dependência do valor fixo.

---

### 4. Nome de Parâmetro/Comportamento Duplicado Logicamente (Data Clump parcial / parâmetro frágil)

**Onde:** `def measure_execution_time(runs=10):`

**Justificativa:** O parâmetro `runs` é o único ponto de configuração do comportamento, mas seu valor está acoplado ao cálculo final (`total_time / runs`) sem qualquer validação. Se `runs = 0`, há divisão por zero. Esse é um cheiro de **design frágil por valor padrão não validado**, próximo a "código sem tratamento de caso de borda".

---

### 5. Instanciação Repetida dentro de Loop sem Reuso (Recurso de curta duração / Criação desnecessária — "Temporary Field" adjacente)

**Onde:**
```python
for _ in range(runs):
    ...
    shop = Shop()
    customer = Customer(shop)
    customer.order_pizza("Cheese")
    customer.complain("The pizza is too cold.")
```

**Justificativa:** A cada iteração cria-se um novo `Shop` e um novo `Customer`, e o objeto `customer` é usado imediatamente e descartado. Cada iteração é independente e descartável. Embora isso seja intencional para medir tempo (cada execução parte de estado limpo), do ponto de vista de design o padrão configura **objetos locais de vida curtíssima cuja única finalidade é disparar efeitos colaterais** — sintoma típico de acoplamento e ausência de abstração de "caso de uso/teste". É o padrão que costuma acompanhar smells como *Feature Envy* nas classes `Shop`/`Customer` (não visíveis aqui).

---

### 6. Strings Mágicas (Magic Strings)

**Onde:**
```python
customer.order_pizza("Cheese")
customer.complain("The pizza is too cold.")
```

**Justificativa:** Literais de string `"Cheese"` e `"The pizza is too cold."` aparecem diretamente embutidos, sem constante nomeada. São "magic strings": o significado (sabor da pizza, texto da reclamação) fica implícito no literal, e qualquer mudança de domínio exigiria editar o corpo do loop. Isso é o equivalente textual do magic number.

---

### 7. Variável de Acumulação e Métrica de Tempo sem Encapsulamento (Long Method aparente / responsabilidade mista)

**Onde:** Corpo inteiro de `measure_execution_time`:
```python
total_time = 0
...
total_time += execution_time
average_time = total_time / runs
return average_time
```

**Justificativa:** A função acumula manualmente o tempo total e calcula a média, combinando duas responsabilidades: (i) orquestrar a execução do fluxo de negócio (`Shop`/`Customer`) e (ii) realizar aritmética de medição. Há uma mistura de "instrumentação de benchmark" com "lógica de domínio". Isso caracteriza o smell de **múltiplas responsabilidades em um único método** (coesão baixa / *Divergent Change* em potencial).

---

### 8. Saída via `print` em vez de retorno/registro (uso de `print` como I/O misturado — "Print Debugging")

**Onde:** No `if __name__ == "__main__":`
```python
print(f"Average execution time over multiple runs: {avg_time} seconds")
```

**Justificativa:** O resultado é comunicado por `print` direto para `stdout`, misturando apresentação com execução no mesmo módulo. Não há separação de I/O (ex.: logging, retorno estruturado). O padrão é o smell de **mistura de apresentação e lógica em ponto de entrada**, que dificulta teste e reuso do cálculo.

---

### 9. Vínculo Temporal / Ordem Obrigatória de Chamadas (Temporal Coupling / Sequential Coupling)

**Onde:**
```python
customer = Customer(shop)
customer.order_pizza("Cheese")
customer.complain("The pizza is too cold.")
```

**Justificativa:** As chamadas precisam ocorrer exatamente nesta ordem, e dependem do estado prévio (`order_pizza` antes de `complain`). Não há verificação nem encapsulamento dessa sequência — um `Customer` pode ser criado e `complain` chamado antes de qualquer pedido sem que o código aqui impeça. A imposição de ordem por convenção, sem proteção, é o smell de **Temporal Coupling** (acoplamento temporal / dependência de ordem de chamadas).

---

## Resumo

| # | Code Smell | Local | Motivo resumido |
|---|-----------|-------|-----------------|
| 1 | Código Morto / String-literal | Todo o arquivo (dentro de `"""..."""`) | Código não executável, encerrado em literal de string |
| 3 | Número Mágico | `runs=10` | Literal sem nome simbólico |
| 4 | Valor padrão frágil | `total_time / runs` | Divisão sem validação de `runs` |
| 5 | Objetos descartáveis no loop | loop `for _ in range(runs)` | Criação/descarte repetido com efeitos colaterais |
| 6 | Strings Mágicas | `"Cheese"`, `"The pizza is too cold."` | Literais sem constante nomeada |
| 7 | Baixa coesão / múltiplas responsabilidades | `measure_execution_time` | Orquestração + aritmética de medição juntas |
| 8 | `print` como saída / mistura de I/O | bloco `__main__` | Apresentação acoplada à execução |
| 9 | Temporal Coupling | sequência `order_pizza` → `complain` | Ordem obrigatória sem encapsulamento |

## Ressalva importante

A descrição do arquivo indica explicitamente que **"This dataset contains smelly code for research and refactoring purposes"** — ou seja, trata-se de um dataset acadêmico de smells. No entanto, **os smells provavelmente mais graves** (como *God Class*, *Feature Envy*, *Shotgun Surgery*, *Long Parameter List*, *Data Class*, entre outros definidos por Fowler) residem muito possivelmente nas classes `Shop` e `Customer`, que **não foram incluídas no material analisado**. Sem o código-fonte dessas classes, não posso afirmar quais smells internos elas contêm.

Se você puder compartilhar os arquivos `Shop.py` e `Customer.py`, posso completar a análise e identificar os smells nas classes de domínio.