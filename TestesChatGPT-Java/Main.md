# Análise de Code Smells — Classe `main` (Java)

## 1. Magic Number (Número Mágico)

**Localização:** Método `measureExecutionTime()`.

**Trecho:**
```java
int runs = 10;
```

**Justificativa:** O valor `10` é utilizado diretamente para definir a quantidade de execuções do teste, sem uma explicação explícita sobre a escolha desse número. Isso pode dificultar a compreensão e a manutenção do código.

## 2. Unnecessary Complexity (Complexidade Desnecessária)

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

**Justificativa:** O código utiliza uma lista para armazenar todos os tempos de execução e posteriormente percorre essa estrutura apenas para calcular a soma. Essa abordagem introduz uma estrutura de dados e um laço adicionais, aumentando desnecessariamente a complexidade do método.

## Conclusão

Foram identificados dois possíveis code smells no código analisado:

1. **Magic Number:** utilização de um valor numérico diretamente no código.
2. **Unnecessary Complexity:** utilização de uma estrutura de dados e de um processamento adicional que não são necessários para o cálculo realizado.
