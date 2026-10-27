# Análise de Code Smells — Classe `main` (Java)

## 1. Magic Number (Número Mágico)

**Localização:** Método `measureExecutionTime()`.

**Trecho:**
```java
int runs = 10;
```

**Justificativa:** O valor `10` é utilizado diretamente para definir a quantidade de execuções do teste, sem uma explicação explícita sobre a escolha desse número. Isso pode dificultar a compreensão da configuração utilizada.

## 2. Estrutura de Dados Desnecessária (Possível Simplificação)

**Localização:** Método `measureExecutionTime()`.

**Trecho:**
```java
List<Long> executionTimes = new ArrayList<>();

// Dentro do primeiro laço
executionTimes.add(executionTime);

// Segundo laço
double totalExecutionTime = 0;
for (Long time : executionTimes) {
    totalExecutionTime += time;
}
```

**Justificativa:** O código armazena todos os tempos de execução em uma lista, embora posteriormente utilize esses valores apenas para calcular a soma. Essa estrutura adiciona complexidade ao processamento.

**Observação:** Essa característica não corresponde diretamente a um code smell específico do catálogo de Martin Fowler e, portanto, não deve ser contabilizada como uma ocorrência confirmada.

## Conclusão

O código apresenta uma possível ocorrência de **Magic Number**, embora sua classificação dependa do critério adotado para considerar constantes numéricas como code smells.

Não foram identificadas evidências suficientes para classificar o método como **Long Method**, **Duplicated Code**, **Dead Code** ou outros code smells do catálogo de Martin Fowler.

Para uma avaliação restrita aos code smells descritos por Fowler, **não há ocorrências inequívocas identificáveis neste arquivo isoladamente**.
