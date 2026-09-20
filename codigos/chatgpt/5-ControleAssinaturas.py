from datetime import datetime, date, timedelta
import calendar


class Plano:
    def __init__(self, nome, preco_mensal, limite_usuarios):
        self.nome = nome
        self.preco_mensal = preco_mensal
        self.limite_usuarios = limite_usuarios


class Pagamento:
    def __init__(self, valor, data_vencimento, data_pagamento=None):
        self.valor = valor
        self.data_vencimento = data_vencimento
        self.data_pagamento = data_pagamento

    def esta_pago(self):
        return self.data_pagamento is not None

    def esta_atrasado_mais_15_dias(self):
        if self.esta_pago():
            return False

        hoje = date.today()
        atraso = hoje - self.data_vencimento

        return atraso.days > 15


class Cliente:
    STATUS_ATIVO = "ativo"
    STATUS_SUSPENSO = "suspenso"
    STATUS_CANCELADO = "cancelado"

    def __init__(self, nome, identificador, plano, data_inicio):
        self.nome = nome
        self.identificador = identificador
        self.plano = plano
        self.data_inicio = data_inicio
        self.historico_pagamentos = []
        self.status = self.STATUS_ATIVO

    def registrar_pagamento(self, pagamento):
        pagamento.data_pagamento = date.today()
        self.historico_pagamentos.append(pagamento)

        self.verificar_status()

    def adicionar_pagamento_pendente(self, pagamento):
        self.historico_pagamentos.append(pagamento)

    def verificar_status(self):
        if self.status == self.STATUS_CANCELADO:
            return

        possui_atraso = any(
            pagamento.esta_atrasado_mais_15_dias()
            for pagamento in self.historico_pagamentos
        )

        if possui_atraso:
            self.status = self.STATUS_SUSPENSO
        else:
            self.status = self.STATUS_ATIVO

    def cancelar_assinatura(self):
        self.status = self.STATUS_CANCELADO

    def calcular_cobranca_proporcional(self, novo_plano):
        if novo_plano.preco_mensal <= self.plano.preco_mensal:
            return 0

        hoje = date.today()

        dias_no_mes = calendar.monthrange(
            hoje.year,
            hoje.month
        )[1]

        dias_restantes = dias_no_mes - hoje.day

        diferenca_preco = (
            novo_plano.preco_mensal
            - self.plano.preco_mensal
        )

        valor_proporcional = (
            diferenca_preco
            / dias_no_mes
        ) * dias_restantes

        return round(valor_proporcional, 2)

    def alterar_plano(self, novo_plano):
        cobranca_proporcional = self.calcular_cobranca_proporcional(
            novo_plano
        )

        self.plano = novo_plano

        return cobranca_proporcional

    def __str__(self):
        return (
            f"Cliente: {self.nome} | "
            f"ID: {self.identificador} | "
            f"Plano: {self.plano.nome} | "
            f"Status: {self.status}"
        )


class SistemaAssinaturas:
    def __init__(self):
        self.clientes = []

        self.planos = {
            "Básico": Plano(
                "Básico",
                29.90,
                1
            ),
            "Premium": Plano(
                "Premium",
                49.90,
                3
            ),
            "Família": Plano(
                "Família",
                79.90,
                6
            )
        }

    def cadastrar_cliente(
        self,
        nome,
        identificador,
        nome_plano,
        data_inicio
    ):
        if self.buscar_cliente(identificador):
            print("Já existe um cliente com esse identificador.")
            return None

        plano = self.planos.get(nome_plano)

        if plano is None:
            print("Plano inválido.")
            return None

        cliente = Cliente(
            nome,
            identificador,
            plano,
            data_inicio
        )

        self.clientes.append(cliente)

        print("Cliente cadastrado com sucesso.")

        return cliente

    def buscar_cliente(self, identificador):
        for cliente in self.clientes:
            if cliente.identificador == identificador:
                return cliente

        return None

    def alterar_plano(self, identificador, nome_novo_plano):
        cliente = self.buscar_cliente(identificador)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        novo_plano = self.planos.get(nome_novo_plano)

        if novo_plano is None:
            print("Plano inválido.")
            return

        if cliente.status == Cliente.STATUS_CANCELADO:
            print("Não é possível alterar o plano de uma assinatura cancelada.")
            return

        cobranca = cliente.alterar_plano(novo_plano)

        print(
            f"Plano alterado para {novo_plano.nome}."
        )

        if cobranca > 0:
            print(
                f"Cobrança proporcional: R$ {cobranca:.2f}"
            )

    def registrar_pagamento(
        self,
        identificador,
        valor,
        data_vencimento
    ):
        cliente = self.buscar_cliente(identificador)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        if cliente.status == Cliente.STATUS_CANCELADO:
            print("Assinatura cancelada.")
            return

        pagamento = Pagamento(
            valor,
            data_vencimento
        )

        cliente.registrar_pagamento(pagamento)

        print("Pagamento registrado com sucesso.")

    def registrar_pagamento_pendente(
        self,
        identificador,
        valor,
        data_vencimento
    ):
        cliente = self.buscar_cliente(identificador)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        pagamento = Pagamento(
            valor,
            data_vencimento
        )

        cliente.adicionar_pagamento_pendente(pagamento)
        cliente.verificar_status()

    def pagar_pendencia(self, identificador):
        cliente = self.buscar_cliente(identificador)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        for pagamento in cliente.historico_pagamentos:
            if not pagamento.esta_pago():
                pagamento.data_pagamento = date.today()

        cliente.verificar_status()

        print("Pagamentos pendentes registrados.")

    def cancelar_assinatura(self, identificador):
        cliente = self.buscar_cliente(identificador)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        cliente.cancelar_assinatura()

        print("Assinatura cancelada com sucesso.")

    def atualizar_status_clientes(self):
        for cliente in self.clientes:
            cliente.verificar_status()

    def gerar_relatorio(self, data_inicio, data_fim):
        self.atualizar_status_clientes()

        ativos = []
        suspensos = []
        cancelados = []

        valor_total_recebido = 0

        for cliente in self.clientes:
            if cliente.status == Cliente.STATUS_ATIVO:
                ativos.append(cliente)

            elif cliente.status == Cliente.STATUS_SUSPENSO:
                suspensos.append(cliente)

            elif cliente.status == Cliente.STATUS_CANCELADO:
                cancelados.append(cliente)

            for pagamento in cliente.historico_pagamentos:
                if pagamento.data_pagamento is not None:
                    if (
                        data_inicio
                        <= pagamento.data_pagamento
                        <= data_fim
                    ):
                        valor_total_recebido += pagamento.valor

        return {
            "ativos": ativos,
            "suspensos": suspensos,
            "cancelados": cancelados,
            "valor_total_recebido": valor_total_recebido
        }


# Exemplo de uso

sistema = SistemaAssinaturas()


# Cadastro de clientes

cliente1 = sistema.cadastrar_cliente(
    "Patricia",
    "C001",
    "Básico",
    date(2026, 9, 1)
)

cliente2 = sistema.cadastrar_cliente(
    "Carlos",
    "C002",
    "Premium",
    date(2026, 8, 15)
)

cliente3 = sistema.cadastrar_cliente(
    "Ana",
    "C003",
    "Família",
    date(2026, 7, 10)
)


# Registro de pagamento realizado

sistema.registrar_pagamento(
    "C001",
    29.90,
    date(2026, 9, 5)
)


# Criando pagamento atrasado há mais de 15 dias

vencimento_antigo = date.today() - timedelta(days=20)

sistema.registrar_pagamento_pendente(
    "C002",
    49.90,
    vencimento_antigo
)


# Verificando situação do cliente

print("\nSituação dos clientes:")

for cliente in sistema.clientes:
    print(cliente)


# Pagando a pendência e reativando assinatura

sistema.pagar_pendencia("C002")


# Mudança de plano

sistema.alterar_plano(
    "C001",
    "Família"
)


# Cancelamento de assinatura

sistema.cancelar_assinatura(
    "C003"
)


# Relatório

inicio_periodo = date(2026, 9, 1)
fim_periodo = date(2026, 9, 30)

relatorio = sistema.gerar_relatorio(
    inicio_periodo,
    fim_periodo
)


print("\nClientes ativos:")

for cliente in relatorio["ativos"]:
    print(cliente.nome)


print("\nClientes suspensos:")

for cliente in relatorio["suspensos"]:
    print(cliente.nome)


print("\nClientes cancelados:")

for cliente in relatorio["cancelados"]:
    print(cliente.nome)


print(
    "\nValor total recebido no período: "
    f"R$ {relatorio['valor_total_recebido']:.2f}"
)