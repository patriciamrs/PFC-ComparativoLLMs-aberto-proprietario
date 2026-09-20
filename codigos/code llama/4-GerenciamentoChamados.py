from datetime import datetime, timedelta

class Chamado:
    def __init__(self, identificador, usuario_solicitante, descricao_problema, prioridade, categoria, data_abertura):
        self.identificador = identificador
        self.usuario_solicitante = usuario_solicitante
        self.descricao_problema = descricao_problema
        self.prioridade = prioridade
        self.categoria = categoria
        self.data_abertura = datetime.strptime(data_abertura, '%Y-%m-%d %H:%M:%S')
        self.responsavel = None
        self.status = 'aberto'
        self.atrasado = False

    def alterar_prioridade(self, nova_prioridade):
        self.prioridade = nova_prioridade

    def atribuir_responsavel(self, responsavel):
        self.responsavel = responsavel

    def atualizar_status(self, novo_status):
        self.status = novo_status

    def verificar_atraso(self):
        if self.status == 'aberto' and self.responsavel is None and (datetime.now() - self.data_abertura).total_seconds() / 3600 > 48:
            self.atrasado = True


class Sistema:
    def __init__(self):
        self.chamados = []

    def criar_chamado(self, chamado):
        self.chamados.append(chamado)

    def consultar_chamados_por_usuario(self, usuario):
        return [chamado for chamado in self.chamados if chamado.usuario_solicitante == usuario]

    def consultar_chamados_por_responsavel(self, responsavel):
        return [chamado for chamado in self.chamados if chamado.responsavel == responsavel]

    def consultar_chamados_por_categoria(self, categoria):
        return [chamado for chamado in self.chamados if chamado.categoria == categoria]

    def consultar_chamados_por_status(self, status):
        return [chamado for chamado in self.chamados if chamado.status == status]

    def gerar_resumo(self):
        prioridades = {'baixa': 0, 'média': 0, 'alta': 0, 'crítica': 0}
        status = {'aberto': 0, 'em atendimento': 0, 'aguardando usuário': 0, 'concluído': 0}
        for chamado in self.chamados:
            prioridades[chamado.prioridade] += 1
            status[chamado.status] += 1
        return prioridades, status


# Exemplo de uso
sistema = Sistema()

chamado1 = Chamado('001', 'Usuário 1', 'Descrição do problema 1', 'crítica', 'Categoria 1', '2024-09-01 10:00:00')
chamado2 = Chamado('002', 'Usuário 2', 'Descrição do problema 2', 'alta', 'Categoria 2', '2024-09-02 11:00:00')

sistema.criar_chamado(chamado1)
sistema.criar_chamado(chamado2)

chamado1.atribuir_responsavel('Responsável 1')
chamado2.atribuir_responsavel('Responsável 2')

chamado1.atualizar_status('em atendimento')
chamado2.atualizar_status('aguardando usuário')

chamado1.verificar_atraso()
chamado2.verificar_atraso()

prioridades, status = sistema.gerar_resumo()
print(f'Prioridades: {prioridades}')
print(f'Status: {status}')

chamados_usuario1 = sistema.consultar_chamados_por_usuario('Usuário 1')
print(f'Chamados do usuário 1: {[chamado.identificador for chamado in chamados_usuario1]}')

chamados_responsavel1 = sistema.consultar_chamados_por_responsavel('Responsável 1')
print(f'Chamados do responsável 1: {[chamado.identificador for chamado in chamados_responsavel1]}')

chamados_categoria1 = sistema.consultar_chamados_por_categoria('Categoria 1')
print(f'Chamados da categoria 1: {[chamado.identificador for chamado in chamados_categoria1]}')

chamados_status_aberto = sistema.consultar_chamados_por_status('aberto')
print(f'Chamados com status aberto: {[chamado.identificador for chamado in chamados_status_aberto]}')