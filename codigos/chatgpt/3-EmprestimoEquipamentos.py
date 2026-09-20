class Equipamento:
    def __init__(self, codigo, nome, categoria, estado_conservacao):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.estado_conservacao = estado_conservacao
        self.situacao = "disponível"

    def __str__(self):
        return (
            f"Código: {self.codigo} | "
            f"Nome: {self.nome} | "
            f"Categoria: {self.categoria} | "
            f"Estado: {self.estado_conservacao} | "
            f"Situação: {self.situacao}"
        )


class Usuario:
    def __init__(self, nome, matricula, limite_maximo):
        self.nome = nome
        self.matricula = matricula
        self.limite_maximo = limite_maximo
        self.equipamentos_emprestados = []

    def pode_emprestar(self):
        return len(self.equipamentos_emprestados) < self.limite_maximo

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Matrícula: {self.matricula} | "
            f"Limite: {self.limite_maximo}"
        )


class SistemaLaboratorio:
    def __init__(self):
        self.equipamentos = []
        self.usuarios = []

    def cadastrar_equipamento(self, equipamento):
        self.equipamentos.append(equipamento)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_equipamento(self, codigo):
        for equipamento in self.equipamentos:
            if equipamento.codigo == codigo:
                return equipamento

        return None

    def buscar_usuario(self, matricula):
        for usuario in self.usuarios:
            if usuario.matricula == matricula:
                return usuario

        return None

    def registrar_emprestimo(self, matricula, codigo_equipamento):
        usuario = self.buscar_usuario(matricula)
        equipamento = self.buscar_equipamento(codigo_equipamento)

        if usuario is None:
            print("Usuário não encontrado.")
            return False

        if equipamento is None:
            print("Equipamento não encontrado.")
            return False

        if equipamento.situacao != "disponível":
            print("Equipamento não está disponível para empréstimo.")
            return False

        if not usuario.pode_emprestar():
            print("Usuário atingiu o limite máximo de equipamentos emprestados.")
            return False

        equipamento.situacao = "emprestado"
        usuario.equipamentos_emprestados.append(equipamento)

        print("Empréstimo realizado com sucesso.")
        return True

    def registrar_devolucao(
        self,
        matricula,
        codigo_equipamento,
        apresentou_problema=False
    ):
        usuario = self.buscar_usuario(matricula)
        equipamento = self.buscar_equipamento(codigo_equipamento)

        if usuario is None:
            print("Usuário não encontrado.")
            return False

        if equipamento is None:
            print("Equipamento não encontrado.")
            return False

        if equipamento not in usuario.equipamentos_emprestados:
            print("Este equipamento não está emprestado para esse usuário.")
            return False

        usuario.equipamentos_emprestados.remove(equipamento)

        if apresentou_problema:
            equipamento.situacao = "manutenção"
        else:
            equipamento.situacao = "disponível"

        print("Devolução realizada com sucesso.")
        return True

    def consultar_equipamentos_usuario(self, matricula):
        usuario = self.buscar_usuario(matricula)

        if usuario is None:
            print("Usuário não encontrado.")
            return []

        return usuario.equipamentos_emprestados

    def listar_equipamentos_indisponiveis(self):
        indisponiveis = []

        for equipamento in self.equipamentos:
            if equipamento.situacao != "disponível":
                indisponiveis.append(equipamento)

        return indisponiveis


# Exemplo de uso

sistema = SistemaLaboratorio()


# Cadastro de equipamentos

equipamento1 = Equipamento(
    "E001",
    "Notebook Dell",
    "Informática",
    "Bom"
)

equipamento2 = Equipamento(
    "E002",
    "Projetor Epson",
    "Audiovisual",
    "Ótimo"
)

equipamento3 = Equipamento(
    "E003",
    "Multímetro",
    "Eletrônica",
    "Regular"
)

sistema.cadastrar_equipamento(equipamento1)
sistema.cadastrar_equipamento(equipamento2)
sistema.cadastrar_equipamento(equipamento3)


# Cadastro de usuários

usuario1 = Usuario(
    "Patricia",
    "2026001",
    2
)

usuario2 = Usuario(
    "Carlos",
    "2026002",
    1
)

sistema.cadastrar_usuario(usuario1)
sistema.cadastrar_usuario(usuario2)


# Registro de empréstimos

sistema.registrar_emprestimo(
    "2026001",
    "E001"
)

sistema.registrar_emprestimo(
    "2026001",
    "E002"
)

# Esta tentativa deve falhar,
# pois Patricia já atingiu o limite de 2 equipamentos.

sistema.registrar_emprestimo(
    "2026001",
    "E003"
)


# Consulta dos equipamentos emprestados

print("\nEquipamentos emprestados para Patricia:")

emprestados = sistema.consultar_equipamentos_usuario(
    "2026001"
)

for equipamento in emprestados:
    print(equipamento)


# Devolução sem problema

sistema.registrar_devolucao(
    "2026001",
    "E001",
    apresentou_problema=False
)


# Devolução com problema

sistema.registrar_devolucao(
    "2026001",
    "E002",
    apresentou_problema=True
)


# Novo empréstimo após a devolução

sistema.registrar_emprestimo(
    "2026002",
    "E003"
)


# Lista de equipamentos indisponíveis

print("\nEquipamentos indisponíveis:")

indisponiveis = sistema.listar_equipamentos_indisponiveis()

for equipamento in indisponiveis:
    print(equipamento)