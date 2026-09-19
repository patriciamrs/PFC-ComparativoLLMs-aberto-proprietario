## Os prompts utilizados para esta pesquisa foram os seguintes:

### 1. SISTEMA DE RESERVA DE SALAS
Desenvolva uma solução em Python para gerenciar reservas de salas em uma empresa.
A solução deve permitir cadastrar salas com nome, capacidade máxima e recursos disponíveis, como projetor, televisão e videoconferência. Também deve permitir cadastrar reservas informando solicitante, sala, data, horário de início, horário de término e quantidade de participantes.
O sistema deve impedir reservas em horários conflitantes para a mesma sala, impedir reservas cuja quantidade de participantes ultrapasse a capacidade da sala e permitir consultar todas as reservas de uma determinada sala em uma data específica.
Além disso, deve ser possível cancelar uma reserva e gerar um relatório com a quantidade total de horas reservadas por sala.
Retorne o código completo necessário para atender ao problema proposto.

### 2. CONTROLE DE PEDIDOS DE RESTAURANTE 
Desenvolva uma solução em Python para controlar pedidos realizados em um restaurante.
Cada pedido deve possuir um número identificador, nome do cliente, lista de itens, quantidade de cada item, preço unitário e tipo de atendimento, que pode ser retirada no local ou entrega.
O sistema deve calcular o valor total do pedido considerando as seguintes regras: pedidos acima de R$ 100,00 recebem 5% de desconto; clientes que informarem um cupom válido recebem mais 10% de desconto; pedidos para entrega possuem uma taxa variável de acordo com a distância informada.
Também deve ser possível adicionar e remover itens de um pedido, alterar quantidades e consultar todos os pedidos realizados por determinado cliente.
Ao final, o sistema deve gerar um resumo contendo subtotal, descontos aplicados, taxa de entrega e valor final.
Retorne o código completo necessário para atender ao problema proposto.

### 3. SISTEMA DE EMPRESTIMO DE EQUIPAMENTOS
Desenvolva uma solução em Python para controlar empréstimos de equipamentos de um laboratório.
Cada equipamento deve possuir código, nome, categoria, estado de conservação e situação, podendo estar disponível, emprestado ou em manutenção.
Os usuários devem possuir nome, matrícula e limite máximo de equipamentos que podem manter emprestados simultaneamente.
O sistema deve permitir registrar empréstimos e devoluções. Um empréstimo só pode ocorrer se o equipamento estiver disponível e se o usuário não tiver atingido seu limite.
Durante a devolução, deve ser possível informar se o equipamento apresentou algum problema. Caso apresente, sua situação deverá ser alterada para manutenção.
O sistema também deve permitir consultar os equipamentos atualmente emprestados por cada usuário e gerar uma lista de todos os equipamentos indisponíveis.
Retorne o código completo necessário para atender ao problema proposto.

### 4. GERENCIAMENTO DE CHAMADOS DE SUPORTE
Desenvolva uma solução em Python para gerenciar chamados de suporte técnico de uma empresa.
Cada chamado deve possuir identificador, usuário solicitante, descrição do problema, prioridade, categoria, data de abertura, responsável pelo atendimento e status.
As prioridades possíveis são baixa, média, alta e crítica. O status pode ser aberto, em atendimento, aguardando usuário ou concluído.
O sistema deve permitir criar chamados, alterar prioridade, atribuir um responsável e atualizar o status.
Chamados críticos devem receber prioridade na listagem. Chamados que permanecerem abertos por mais de 48 horas sem responsável devem ser identificados como atrasados.
Também deve ser possível consultar chamados por usuário, responsável, categoria e status, além de gerar um resumo contendo a quantidade de chamados em cada prioridade e status.
Retorne o código completo necessário para atender ao problema proposto.

### 5. CONTROLE DE ASSINATURAS DE SERVIÇO DIGITAL
Desenvolva uma solução em Python para administrar assinaturas de um serviço digital.
Cada cliente deve possuir nome, identificador, plano contratado, data de início da assinatura e histórico de pagamentos.
Os planos disponíveis são Básico, Premium e Família, cada um com preço mensal e limite diferente de usuários.
O sistema deve permitir cadastrar clientes, alterar planos, registrar pagamentos e cancelar assinaturas.
Caso o cliente possua um pagamento atrasado há mais de 15 dias, a assinatura deverá ser marcada como suspensa. Ao registrar o pagamento pendente, a assinatura poderá ser reativada.
Mudanças para um plano mais caro devem gerar uma cobrança proporcional ao número de dias restantes no mês.
O sistema também deve gerar um relatório informando clientes ativos, suspensos e cancelados, além do valor total recebido no período.
Retorne o código completo necessário para atender ao problema proposto.

### 6. SISTEMA DE CONTROLE DE ENTREGAS
Desenvolva uma solução em Python para controlar entregas realizadas por uma transportadora.
Cada entrega deve possuir código, cliente, endereço de origem, endereço de destino, peso da encomenda, distância da entrega, data prevista e status. Os status possíveis são aguardando coleta, em transporte, entregue e cancelada.
O preço da entrega deve ser calculado levando em consideração o peso e a distância. Entregas com peso superior a 20 kg devem possuir uma taxa adicional. Entregas cuja distância seja superior a 200 km também recebem uma taxa adicional.
O sistema deve permitir atualizar o status da entrega, impedir que uma entrega cancelada seja alterada novamente e registrar atrasos quando a entrega não for concluída até a data prevista.
Também deve permitir consultar entregas por cliente e gerar um relatório contendo o valor total das entregas e a quantidade de entregas em cada status.
Retorne o código completo necessário para atender ao problema proposto.

### 7. GESTÃO DE INSCRIÇÃO EM EVENTOS
Desenvolva uma solução em Python para gerenciar inscrições em eventos e atividades.
Cada evento deve possuir nome, data, capacidade máxima e uma lista de atividades disponíveis. Cada atividade deve possuir nome, horário e limite próprio de participantes. Um participante deve possuir nome, e-mail e as atividades nas quais está inscrito.
O sistema deve impedir novas inscrições quando a capacidade máxima do evento for atingida. Também deve impedir que um participante se inscreva em duas atividades que ocorram no mesmo horário ou em uma atividade que já tenha atingido seu limite.
Deve ser possível cancelar uma inscrição, trocar uma atividade e consultar todas as atividades de determinado participante.
Ao final, o sistema deve gerar um relatório contendo número de inscritos no evento, ocupação de cada atividade e participantes que não escolheram nenhuma atividade.
Retorne o código completo necessário para atender ao problema proposto.

### 8. SISTEMA DE CONTROLE DE ESTOQUE COM MULTIPLOS FORNECEDORES
Desenvolva uma solução em Python para gerenciar o estoque de produtos de uma pequena empresa.
Cada produto deve possuir código, nome, categoria, quantidade atual, quantidade mínima e uma lista de fornecedores. Cada fornecedor deve possuir nome, prazo médio de entrega e preço praticado para o produto.
O sistema deve permitir registrar entradas e saídas de produtos. Não deve ser permitida uma saída superior à quantidade disponível em estoque.
Quando a quantidade de um produto ficar abaixo do estoque mínimo, o sistema deverá indicar a necessidade de reposição e selecionar um fornecedor considerando preço e prazo de entrega.
Caso dois fornecedores apresentem o mesmo preço, deve ser escolhido aquele com menor prazo. Caso apresentem o mesmo prazo, deve ser escolhido aquele com menor preço.
O sistema também deve permitir consultar produtos por categoria e gerar um relatório contendo produtos abaixo do estoque mínimo, valor total estimado do estoque e fornecedor recomendado para cada item que necessita de reposição.
Retorne o código completo necessário para atender ao problema proposto.