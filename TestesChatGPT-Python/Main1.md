
## Análise de Code Smells — `main.py`

Após analisar o código apresentado, **não foram identificados code smells evidentes** que possam ser classificados com segurança segundo o catálogo de Martin Fowler.

A função `measure_execution_time()` possui uma responsabilidade bem definida: medir o tempo médio de execução de uma sequência de operações. Sua estrutura é relativamente simples, sem duplicações significativas, métodos excessivamente longos ou condicionais complexas.

### Possível ocorrência: Magic Number

**Localização:** Parâmetro `runs=10` da função `measure_execution_time()`.

```python
def measure_execution_time(runs=10):
```

**Justificativa:** O valor literal `10` estabelece a quantidade padrão de execuções. Embora possa ser considerado um *Magic Number* em algumas classificações, seu significado é compreensível pelo nome do parâmetro. Portanto, não há evidência suficiente para classificá-lo como um problema de manutenção.

Além disso, *Magic Number* não é tratado como um smell independente no catálogo clássico de Fowler.

### Conclusão

**Nenhum code smell confirmado.**

O código apresenta uma estrutura simples e organizada, sem evidências suficientes para afirmar a presença de smells como *Long Method*, *Duplicated Code*, *Feature Envy* ou *Dead Code*.

Essa conclusão considera apenas o trecho fornecido, sem avaliar a implementação das classes `Shop` e `Customer`.
