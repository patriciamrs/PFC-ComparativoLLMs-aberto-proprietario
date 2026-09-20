class Atividade:
    def __init__(self, nome, horario, limite_participantes):
        self.nome = nome
        self.horario = horario
        self.limite_participantes = limite_participantes
        self.participantes = []

    def possui_vaga(self):
        return len(self.participantes) < self.limite_participantes

    def adicionar_participante(self, participante):
        if not self.possui_vaga():
            return False

        self.participantes.append(participante)
        return True

    def remover_participante(self, participante):
        if participante in self.participantes:
            self.participantes.remove(participante)
            return True

        return False


class Participante:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.atividades = []

    def possui_conflito_horario(self, atividade):
        for atividade_inscrita in self.atividades:
            if atividade_inscrita.horario == atividade.horario:
                return True

        return False

    def __str__(self):
        return f"{self.nome} - {self.email}"


class Evento:
    def __init__(self, nome, data, capacidade_maxima):
        self.nome = nome
        self.data = data
        self.capacidade_maxima = capacidade_maxima
        self.atividades = []
        self.participantes = []

    def adicionar_atividade(self, atividade):
        self.atividades.append(atividade)

    def buscar_atividade(self, nome_atividade):
        for atividade in self.atividades:
            if atividade.nome == nome_atividade:
                return atividade

        return None

    def buscar_participante(self, email):
        for participante in self.participantes:
            if participante.email == email:
                return participante

        return None

    def inscrever_participante(self, participante):
        if self.buscar_participante(participante.email):
            print("Participante já está inscrito no evento.")
            return False

        if len(self.participantes) >= self.capacidade_maxima:
            print("Capacidade máxima do evento atingida.")
            return False

        self.participantes.append(participante)

        print("Participante inscrito no evento com sucesso.")
        return True

    def inscrever_em_atividade(self, email, nome_atividade):
        participante = self.buscar_participante(email)

        if participante is None:
            print("Participante não está inscrito no evento.")
            return False

        atividade = self.buscar_atividade(nome_atividade)

        if atividade is None:
            print("Atividade não encontrada.")
            return False

        if atividade in participante.atividades:
            print("Participante já está inscrito nessa atividade.")
            return False

        if not atividade.possui_vaga():
            print("Atividade atingiu o limite de participantes.")
            return False

        if participante.possui_conflito_horario(atividade):
            print("Participante já possui outra atividade nesse horário.")
            return False

        participante.atividades.append(atividade)
        atividade.adicionar_participante(participante)

        print("Inscrição na atividade realizada com sucesso.")
        return True

    def cancelar_inscricao_atividade(self, email, nome_atividade):
        participante = self.buscar_participante(email)

        if participante is None:
            print("Participante não encontrado.")
            return False

        atividade = self.buscar_atividade(nome_atividade)

        if atividade is None:
            print("Atividade não encontrada.")
            return False

        if atividade not in participante.atividades:
            print("Participante não está inscrito nessa atividade.")
            return False

        participante.atividades.remove(atividade)
        atividade.remover_participante(participante)

        print("Inscrição na atividade cancelada com sucesso.")
        return True

    def trocar_atividade(
        self,
        email,
        atividade_atual_nome,
        nova_atividade_nome
    ):
        participante = self.buscar_participante(email)

        if participante is None:
            print("Participante não encontrado.")
            return False

        atividade_atual = self.buscar_atividade(
            atividade_atual_nome
        )

        nova_atividade = self.buscar_atividade(
            nova_atividade_nome
        )

        if atividade_atual is None or nova_atividade is None:
            print("Atividade não encontrada.")
            return False

        if atividade_atual not in participante.atividades:
            print("Participante não está inscrito na atividade atual.")
            return False

        if not nova_atividade.possui_vaga():
            print("Nova atividade atingiu o limite de participantes.")
            return False

        for atividade in participante.atividades:
            if (
                atividade != atividade_atual
                and atividade.horario == nova_atividade.horario
            ):
                print(
                    "Não é possível trocar. "
                    "Existe conflito de horário."
                )
                return False

        participante.atividades.remove(atividade_atual)
        atividade_atual.remover_participante(participante)

        participante.atividades.append(nova_atividade)
        nova_atividade.adicionar_participante(participante)

        print("Atividade trocada com sucesso.")
        return True

    def consultar_atividades_participante(self, email):
        participante = self.buscar_participante(email)

        if participante is None:
            print("Participante não encontrado.")
            return []

        return participante.atividades

    def cancelar_inscricao_evento(self, email):
        participante = self.buscar_participante(email)

        if participante is None:
            print("Participante não encontrado.")
            return False

        for atividade in participante.atividades[:]:
            atividade.remover_participante(participante)

        participante.atividades.clear()
        self.participantes.remove(participante)

        print("Inscrição no evento cancelada com sucesso.")
        return True

    def gerar_relatorio(self):
        ocupacao_atividades = {}

        for atividade in self.atividades:
            ocupacao_atividades[atividade.nome] = {
                "inscritos": len(atividade.participantes),
                "limite": atividade.limite_participantes
            }

        sem_atividade = []

        for participante in self.participantes:
            if not participante.atividades:
                sem_atividade.append(participante.nome)

        return {
            "numero_inscritos_evento": len(self.participantes),
            "ocupacao_atividades": ocupacao_atividades,
            "participantes_sem_atividade": sem_atividade
        }


# Exemplo de uso

evento = Evento(
    "Semana de Tecnologia",
    "25/09/2026",
    4
)


# Cadastro de atividades

atividade1 = Atividade(
    "Python",
    "09:00",
    2
)

atividade2 = Atividade(
    "Banco de Dados",
    "10:00",
    3
)

atividade3 = Atividade(
    "Inteligência Artificial",
    "09:00",
    2
)

evento.adicionar_atividade(atividade1)
evento.adicionar_atividade(atividade2)
evento.adicionar_atividade(atividade3)


# Cadastro dos participantes

participante1 = Participante(
    "Patricia",
    "patricia@email.com"
)

participante2 = Participante(
    "Carlos",
    "carlos@email.com"
)

participante3 = Participante(
    "Ana",
    "ana@email.com"
)

participante4 = Participante(
    "João",
    "joao@email.com"
)


# Inscrição no evento

evento.inscrever_participante(participante1)
evento.inscrever_participante(participante2)
evento.inscrever_participante(participante3)
evento.inscrever_participante(participante4)


# Inscrição nas atividades

evento.inscrever_em_atividade(
    "patricia@email.com",
    "Python"
)

evento.inscrever_em_atividade(
    "patricia@email.com",
    "Banco de Dados"
)

evento.inscrever_em_atividade(
    "carlos@email.com",
    "Python"
)

evento.inscrever_em_atividade(
    "ana@email.com",
    "Inteligência Artificial"
)


# Teste de conflito de horário
# Patricia já está em Python às 09:00

evento.inscrever_em_atividade(
    "patricia@email.com",
    "Inteligência Artificial"
)


# Consulta das atividades de Patricia

print("\nAtividades de Patricia:")

atividades = evento.consultar_atividades_participante(
    "patricia@email.com"
)

for atividade in atividades:
    print(
        f"{atividade.nome} - "
        f"{atividade.horario}"
    )


# Troca de atividade

evento.trocar_atividade(
    "carlos@email.com",
    "Python",
    "Banco de Dados"
)


# Cancelamento de atividade

evento.cancelar_inscricao_atividade(
    "patricia@email.com",
    "Banco de Dados"
)


# Relatório

relatorio = evento.gerar_relatorio()

print("\nRelatório do evento:")

print(
    "Número de inscritos no evento:",
    relatorio["numero_inscritos_evento"]
)

print("\nOcupação das atividades:")

for nome, dados in relatorio["ocupacao_atividades"].items():
    print(
        f"{nome}: "
        f"{dados['inscritos']} / "
        f"{dados['limite']}"
    )

print("\nParticipantes sem atividade:")

for participante in relatorio["participantes_sem_atividade"]:
    print(participante)