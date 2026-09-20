class Atividade:
    def __init__(self, nome, horario, limite):
        self.nome = nome
        self.horario = horario
        self.limite = limite
        self.inscritos = []

    def inscrever(self, participante):
        if len(self.inscritos) < self.limite:
            self.inscritos.append(participante)
            return True
        return False

    def cancelar_inscricao(self, participante):
        if participante in self.inscritos:
            self.inscritos.remove(participante)
            return True
        return False


class Evento:
    def __init__(self, nome, data, capacidade_maxima):
        self.nome = nome
        self.data = data
        self.capacidade_maxima = capacidade_maxima
        self.atividades = []
        self.participantes = []

    def adicionar_atividade(self, atividade):
        self.atividades.append(atividade)

    def inscrever_participante(self, participante):
        if len(self.participantes) < self.capacidade_maxima:
            self.participantes.append(participante)
            return True
        return False

    def cancelar_inscricao_participante(self, participante):
        if participante in self.participantes:
            self.participantes.remove(participante)
            return True
        return False


class Participante:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.atividades = []

    def inscrever_atividade(self, atividade, evento):
        if atividade.inscrever(self):
            self.atividades.append(atividade)
            return True
        return False

    def cancelar_inscricao_atividade(self, atividade, evento):
        if atividade.cancelar_inscricao(self):
            self.atividades.remove(atividade)
            return True
        return False

    def trocar_atividade(self, atividade_antiga, atividade_nova, evento):
        if atividade_antiga.cancelar_inscricao(self) and atividade_nova.inscrever(self):
            self.atividades.remove(atividade_antiga)
            self.atividades.append(atividade_nova)
            return True
        return False


class Sistema:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento):
        self.eventos.append(evento)

    def gerar_relatorio(self, evento):
        num_inscritos = len(evento.participantes)
        ocupacao_atividades = {atividade.nome: len(atividade.inscritos) for atividade in evento.atividades}
        participantes_sem_atividade = [participante.nome for participante in evento.participantes if not participante.atividades]
        return num_inscritos, ocupacao_atividades, participantes_sem_atividade


# Exemplo de uso
sistema = Sistema()

evento = Evento("Evento 1", "2024-09-20", 100)
sistema.adicionar_evento(evento)

atividade1 = Atividade("Atividade 1", "10:00", 20)
atividade2 = Atividade("Atividade 2", "11:00", 30)
evento.adicionar_atividade(atividade1)
evento.adicionar_atividade(atividade2)

participante1 = Participante("Participante 1", "participante1@example.com")
participante2 = Participante("Participante 2", "participante2@example.com")

if evento.inscrever_participante(participante1) and evento.inscrever_participante(participante2):
    participante1.inscrever_atividade(atividade1, evento)
    participante2.inscrever_atividade(atividade2, evento)

num_inscritos, ocupacao_atividades, participantes_sem_atividade = sistema.gerar_relatorio(evento)
print(f"Número de inscritos: {num_inscritos}")
print(f"Ocupação das atividades: {ocupacao_atividades}")
print(f"Participantes sem atividade: {participantes_sem_atividade}")