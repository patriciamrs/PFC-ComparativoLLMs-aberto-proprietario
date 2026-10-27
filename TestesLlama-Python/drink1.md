# Análise de Code Smells

## Code Smells Identificados

### 1. Classe com responsabilidade única e fraca (Lazy Class / Classe Preguiçosa)

**Trecho:** Classe `Drink` inteira.

**Justificativa:** A classe tem um propósito muito restrito: armazenar um único atributo (`drink_type`) e imprimir mensagens relacionadas. Ela não implementa comportamentos significativos de domínio — apenas encapsula uma string e a repete em três `print`. Classe cujo escopo é tão reduzido que não justifica sua existência autônoma é caracterizada como *Lazy Class*.

### 2. Atributo não inicializado no construtor (Temporary/Improper Initialization — "Null" inicial)

**Trecho:**
```python
def __init__(self):
    self.drink_type = None
```

**Justificativa:** O atributo `drink_type` é inicializado como `None` no construtor, mas só recebe valor real depois, via `create_order`. Isso deixa o objeto em estado temporariamente inválido (sem tipo de bebida definido), obrigando métodos posteriores a depender de uma chamada anterior para funcionar corretamente. Caso `add_to_order()` ou `confirm_order()` sejam chamados antes de `create_order()`, o comportamento fica incoerente (imprime `None`). Caracteriza inicialização inadequada e estado inconsistente.

### 3. Ordem de chamadas obrigatória entre métodos (Temporal Coupling / Acoplamento Temporal)

**Trecho:** Relação entre `create_order()`, `add_to_order()` e `confirm_order()`.

**Justificativa:** Os três métodos precisam ser invocados numa sequência obrigatória (`create_order` → `add_to_order` → `confirm_order`), mas nada no código impõe ou documenta essa ordem. O correto funcionamento depende de o cliente chamá-los na sequência adequada. Dependência implícita de ordem de execução é *Temporal Coupling*.

### 4. Saída de dados embutida no código de domínio (Código com efeito colateral / I/O espalhado — "Side Effects" / violação de Separation of Concerns)

**Trecho:** Todos os métodos usam `print(...)`:
```python
print(f"Creating order for {drink_type} drink.")
print(f"Adding {self.drink_type} to the order.")
print(f"Order for {self.drink_type} confirmed.")
```

**Justificativa:** A lógica de negócio da classe está misturada com operação de saída (I/O) diretamente nos métodos. Isso caracteriza um *code smell* de responsabilidade misturada — a classe deveria representar o estado/comportamento de domínio e não decidir sobre apresentação. Esse padrão é frequentemente classificado como *Command-Query Separation* violado ou acoplamento a um canal de saída específico (`stdout`).

### 5. Métodos "no-op" / método sem comportamento real (Método sem efeito útil)

**Trecho:** `add_to_order()` e `confirm_order()`.

**Justificativa:** Ambos os métodos não alteram o estado do objeto nem realizam qualquer cálculo; apenas imprimem uma mensagem. Métodos que não executam ação significativa sobre o estado (apenas "ecoam" informação) configuram comportamento superficial, aproximando-se do padrão de *No-op Method* ou métodos sem propósito de domínio real.

> Observação: alguns desses sinais (especialmente os itens 1, 3 e 5) se sobrepõem parcialmente; a classe funciona como um pequeno "holder" de string com métodos de impressão, o que concentra vários indicadores típicos de *Lazy Class* combinados com *Temporal Coupling*.