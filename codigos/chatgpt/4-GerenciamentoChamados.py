from datetime import datetime, timedelta


class Chamado:
    PRIORIDADES = ["baixa", "média", "alta", "crítica"]

    STATUS_VALIDOS = [
        "aberto",
        "em atendimento",
        "aguardando usuário",
        "concluído"
    ]

    def __init__(
        self,
        identificador,
        usuario,
        descricao,
        prioridade,
        categoria,
        data_abertura=None
    ):
        if prioridade not in self.PRIORIDADES:
            raise ValueError("Prioridade inválida.")

        self.identificador = identificador
        self.usuario = usuario
        self.descricao = descricao
        self.prioridade = prioridade
        self.categoria = categoria
        self.data_abertura = data_abertura or datetime.now()
        self.responsavel = None
        self.status = "aberto"

    def alterar_prioridade(self, nova_prioridade):
        if nova_prioridade not in self.PRIORIDADES:
            print("Prioridade inválida.")
            return False

        self.prioridade = nova_prioridade
        return True

    def atribuir_responsavel(self, responsavel):
        self.responsavel = responsavel

    def atualizar_status(self, novo_status):
        if novo_status not in self.STATUS_VALIDOS:
            print("Status inválido.")
            return False

        self.status = novo_status
        return True

    def esta_atrasado(self):
        limite = datetime.now() - timedelta(hours=48)

        return (
            self.status == "aberto"
            and self.responsavel is None
            and self.data_abertura < limite
        )

    def __str__(self):
        responsavel = self.responsavel if self.responsavel else "Não atribuído"

        return (
            f"ID: {self.identificador} | "
            f"Usuário: {self.usuario} | "
            f"Prioridade: {self.prioridade} | "
            f"Categoria: {self.categoria} | "
            f"Status: {self.status} | "
            f"Responsável: {responsavel}"
        )


class SistemaSuporte:
    def __init__(self):
        self.chamados = []

    def criar_chamado(
        self,
        identificador,
        usuario,
        descricao,
        prioridade,
        categoria,
        data_abertura=None
    ):
        if self.buscar_chamado(identificador):
            print("Já existe um chamado com esse identificador.")
            return None

        chamado = Chamado(
            identificador,
            usuario,
            descricao,
            prioridade,
            categoria,
            data_abertura
        )

        self.chamados.append(chamado)

        print("Chamado criado com sucesso.")
        return chamado

    def buscar_chamado(self, identificador):
        for chamado in self.chamados:
            if chamado.identificador == identificador:
                return chamado

        return None

    def alterar_prioridade(self, identificador, nova_prioridade):
        chamado = self.buscar_chamado(identificador)

        if chamado is None:
            print("Chamado não encontrado.")
            return False

        if chamado.alterar_prioridade(nova_prioridade):
            print("Prioridade alterada com sucesso.")
            return True

        return False

    def atribuir_responsavel(self, identificador, responsavel):
        chamado = self.buscar_chamado(identificador)

        if chamado is None:
            print("Chamado não encontrado.")
            return False

        chamado.atribuir_responsavel(responsavel)

        print("Responsável atribuído com sucesso.")
        return True

    def atualizar_status(self, identificador, novo_status):
        chamado = self.buscar_chamado(identificador)

        if chamado is None:
            print("Chamado não encontrado.")
            return False

        if chamado.atualizar_status(novo_status):
            print("Status atualizado com sucesso.")
            return True

        return False

    def listar_chamados(self):
        ordem_prioridade = {
            "crítica": 0,
            "alta": 1,
            "média": 2,
            "baixa": 3
        }

        return sorted(
            self.chamados,
            key=lambda chamado: (
                ordem_prioridade[chamado.prioridade],
                chamado.data_abertura
            )
        )

    def listar_chamados_atrasados(self):
        return [
            chamado
            for chamado in self.chamados
            if chamado.esta_atrasado()
        ]

    def consultar_por_usuario(self, usuario):
        return [
            chamado
            for chamado in self.chamados
            if chamado.usuario.lower() == usuario.lower()
        ]

    def consultar_por_responsavel(self, responsavel):
        return [
            chamado
            for chamado in self.chamados
            if chamado.responsavel is not None
            and chamado.responsavel.lower() == responsavel.lower()
        ]

    def consultar_por_categoria(self, categoria):
        return [
            chamado
            for chamado in self.chamados
            if chamado.categoria.lower() == categoria.lower()
        ]

    def consultar_por_status(self, status):
        return [
            chamado
            for chamado in self.chamados
            if chamado.status.lower() == status.lower()
        ]

    def gerar_resumo(self):
        resumo_prioridades = {
            "baixa": 0,
            "média": 0,
            "alta": 0,
            "crítica": 0
        }

        resumo_status = {
            "aberto": 0,
            "em atendimento": 0,
            "aguardando usuário": 0,
            "concluído": 0
        }

        for chamado in self.chamados:
            resumo_prioridades[chamado.prioridade] += 1
            resumo_status[chamado.status] += 1

        return {
            "prioridades": resumo_prioridades,
            "status": resumo_status
        }


# Exemplo de uso

sistema = SistemaSuporte()


# Criando chamados

sistema.criar_chamado(
    1,
    "Patricia",
    "Computador não liga.",
    "crítica",
    "Hardware"
)

sistema.criar_chamado(
    2,
    "Carlos",
    "Erro ao acessar o sistema.",
    "alta",
    "Software"
)

sistema.criar_chamado(
    3,
    "Ana",
    "Solicitação de instalação de programa.",
    "baixa",
    "Software"
)


# Chamado antigo para testar atraso

data_antiga = datetime.now() - timedelta(hours=60)

sistema.criar_chamado(
    4,
    "João",
    "Impressora não funciona.",
    "média",
    "Hardware",
    data_antiga
)


# Atribuindo responsável

sistema.atribuir_responsavel(
    1,
    "Marcos"
)

sistema.atribuir_responsavel(
    2,
    "Fernanda"
)


# Alterando status

sistema.atualizar_status(
    1,
    "em atendimento"
)

sistema.atualizar_status(
    2,
    "aguardando usuário"
)


# Alterando prioridade

sistema.alterar_prioridade(
    3,
    "média"
)


# Listagem ordenada por prioridade

print("\nChamados ordenados por prioridade:")

for chamado in sistema.listar_chamados():
    print(chamado)


# Chamados atrasados

print("\nChamados atrasados:")

for chamado in sistema.listar_chamados_atrasados():
    print(chamado)


# Consulta por usuário

print("\nChamados da Patricia:")

for chamado in sistema.consultar_por_usuario("Patricia"):
    print(chamado)


# Consulta por responsável

print("\nChamados do responsável Marcos:")

for chamado in sistema.consultar_por_responsavel("Marcos"):
    print(chamado)


# Consulta por categoria

print("\nChamados da categoria Hardware:")

for chamado in sistema.consultar_por_categoria("Hardware"):
    print(chamado)


# Consulta por status

print("\nChamados em atendimento:")

for chamado in sistema.consultar_por_status("em atendimento"):
    print(chamado)


# Resumo

resumo = sistema.gerar_resumo()

print("\nResumo por prioridade:")

for prioridade, quantidade in resumo["prioridades"].items():
    print(f"{prioridade}: {quantidade}")


print("\nResumo por status:")

for status, quantidade in resumo["status"].items():
    print(f"{status}: {quantidade}")