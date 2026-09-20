from datetime import datetime, timedelta

class Plano:
    def __init__(self, nome, preco, limite_usuarios):
        self.nome = nome
        self.preco = preco
        self.limite_usuarios = limite_usuarios

class Cliente:
    def __init__(self, nome, identificador, plano, data_inicio):
        self.nome = nome
        self.identificador = identificador
        self.plano = plano
        self.data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
        self.historico_pagamentos = []
        self.assinatura_suspensa = False
        self.assinatura_cancelada = False

    def alterar_plano(self, novo_plano):
        if self.assinatura_suspensa or self.assinatura_cancelada:
            print('Assinatura suspensa ou cancelada. Não é possível alterar o plano.')
            return
        if novo_plano.preco > self.plano.preco:
            dias_restantes = (datetime.today().replace(day=1) + timedelta(days=32) - timedelta(days=1) - datetime.today()).days
            cobranca_proporcional = (novo_plano.preco - self.plano.preco) / 30 * dias_restantes
            self.historico_pagamentos.append({'data': datetime.today(), 'valor': cobranca_proporcional, 'descricao': 'Cobrança proporcional'})
        self.plano = novo_plano

    def registrar_pagamento(self, data_pagamento, valor):
        self.historico_pagamentos.append({'data': datetime.strptime(data_pagamento, '%Y-%m-%d'), 'valor': valor, 'descricao': 'Pagamento mensal'})
        if self.assinatura_suspensa:
            self.assinatura_suspensa = False

    def cancelar_assinatura(self):
        self.assinatura_cancelada = True

    def verificar_pagamento_atrasado(self):
        if self.historico_pagamentos:
            ultimo_pagamento = self.historico_pagamentos[-1]['data']
            if (datetime.today() - ultimo_pagamento).days > 15:
                self.assinatura_suspensa = True

class Sistema:
    def __init__(self):
        self.clientes = []
        self.planos = [
            Plano('Básico', 19.99, 1),
            Plano('Premium', 29.99, 5),
            Plano('Família', 49.99, 10)
        ]

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def gerar_relatorio(self):
        clientes_ativos = [cliente for cliente in self.clientes if not cliente.assinatura_suspensa and not cliente.assinatura_cancelada]
        clientes_suspensos = [cliente for cliente in self.clientes if cliente.assinatura_suspensa]
        clientes_cancelados = [cliente for cliente in self.clientes if cliente.assinatura_cancelada]
        valor_total_recebido = sum(sum(pagamento['valor'] for pagamento in cliente.historico_pagamentos) for cliente in self.clientes)
        return clientes_ativos, clientes_suspensos, clientes_cancelados, valor_total_recebido


# Exemplo de uso
sistema = Sistema()

cliente1 = Cliente('Cliente 1', '001', sistema.planos[0], '2024-09-01')
cliente2 = Cliente('Cliente 2', '002', sistema.planos[1], '2024-09-01')

sistema.cadastrar_cliente(cliente1)
sistema.cadastrar_cliente(cliente2)

cliente1.registrar_pagamento('2024-09-15', 19.99)
cliente2.registrar_pagamento('2024-09-10', 29.99)

cliente1.alterar_plano(sistema.planos[1])

cliente1.verificar_pagamento_atrasado()
cliente2.verificar_pagamento_atrasado()

clientes_ativos, clientes_suspensos, clientes_cancelados, valor_total_recebido = sistema.gerar_relatorio()
print(f'Clientes ativos: {len(clientes_ativos)}')
print(f'Clientes suspensos: {len(clientes_suspensos)}')
print(f'Clientes cancelados: {len(clientes_cancelados)}')
print(f'Valor total recebido: {valor_total_recebido}')