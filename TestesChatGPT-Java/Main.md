
## Análise de Code Smells — Classe `main`

### 1. Long Function (Método Longo)

- **Localização:** Método `measureExecutionTime()`.
- **Justificativa:** O método concentra diferentes operações, incluindo a execução repetida do código, a medição do tempo de execução, o armazenamento dos resultados e o cálculo da média. Entretanto, essas operações estão relacionadas ao mesmo objetivo e o método possui tamanho moderado. Portanto, não há evidência suficiente para confirmar esse code smell.

### 2. Magic Number (Número Mágico)

- **Localização:** Método `measureExecutionTime()`, na expressão:

```java
return totalExecutionTime / runs / 1_000_000_000.0;
```

- **Justificativa:** O valor numérico `1_000_000_000.0` é utilizado diretamente para converter nanossegundos em segundos. Embora seja um número literal, seu significado está documentado e ele representa um fator de conversão conhecido. Além disso, Magic Number não é um code smell independente no catálogo de Martin Fowler, não sendo suficiente para caracterizar Primitive Obsession neste caso.

### 3. Temporary Field (Campo Temporário)

- **Localização:** Não identificado.
- **Justificativa:** As variáveis utilizadas no método `measureExecutionTime()` são locais e necessárias durante sua execução. Não existem atributos de classe utilizados apenas em determinadas circunstâncias, portanto esse code smell não está presente.

### 4. Middle Man (Intermediário)

- **Localização:** Não identificado.
- **Justificativa:** Embora o método realize chamadas a objetos das classes `Shop` e `Customer`, não há evidências de que a classe `main` atue predominantemente como intermediária na delegação de funcionalidades.

### Conclusão

Não foram identificados code smells que possam ser confirmados com segurança no código apresentado, considerando os critérios descritos por Martin Fowler.
