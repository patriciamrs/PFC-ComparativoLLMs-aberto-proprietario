class Equipamento:
    def __init__(self, codigo, nome, categoria, estado_conservacao):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.estado_conservacao = estado_conservacao
        self.situacao = 'disponível'

    def emprestar(self):
        if self.situacao == 'disponível':
            self.situacao = 'emprestado'
            return True
        return False

    def devolver(self, apresentou_problema):
        if self.situacao == 'emprestado':
            if apresentou_problema:
                self.situacao = 'manutenção'
            else:
                self.situacao = 'disponível'
            return True
        return False


class Usuario:
    def __init__(self, nome, matricula, limite_maximo):
        self.nome = nome
        self.matricula = matricula
        self.limite_maximo = limite_maximo
        self.equipamentos_emprestados = []

    def emprestar_equipamento(self, equipamento):
        if len(self.equipamentos_emprestados) < self.limite_maximo and equipamento.emprestar():
            self.equipamentos_emprestados.append(equipamento)
            return True
        return False

    def devolver_equipamento(self, equipamento, apresentou_problema):
        if equipamento in self.equipamentos_emprestados and equipamento.devolver(apresentou_problema):
            self.equipamentos_emprestados.remove(equipamento)
            return True
        return False


class Sistema:
    def __init__(self):
        self.equipamentos = []
        self.usuarios = []

    def adicionar_equipamento(self, equipamento):
        self.equipamentos.append(equipamento)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def consultar_equipamentos_emprestados_por_usuario(self, usuario):
        return [equipamento.nome for equipamento in usuario.equipamentos_emprestados]

    def gerar_lista_equipamentos_indisponiveis(self):
        return [equipamento.nome for equipamento in self.equipamentos if equipamento.situacao != 'disponível']


# Exemplo de uso
sistema = Sistema()

equipamento1 = Equipamento('001', 'Equipamento 1', 'Categoria 1', 'Bom')
equipamento2 = Equipamento('002', 'Equipamento 2', 'Categoria 2', 'Regular')

sistema.adicionar_equipamento(equipamento1)
sistema.adicionar_equipamento(equipamento2)

usuario1 = Usuario('Usuário 1', '001', 2)
usuario2 = Usuario('Usuário 2', '002', 1)

sistema.adicionar_usuario(usuario1)
sistema.adicionar_usuario(usuario2)

usuario1.emprestar_equipamento(equipamento1)
usuario2.emprestar_equipamento(equipamento2)

print(sistema.consultar_equipamentos_emprestados_por_usuario(usuario1))
print(sistema.consultar_equipamentos_emprestados_por_usuario(usuario2))

usuario1.devolver_equipamento(equipamento1, False)
usuario2.devolver_equipamento(equipamento2, True)

print(sistema.gerar_lista_equipamentos_indisponiveis())