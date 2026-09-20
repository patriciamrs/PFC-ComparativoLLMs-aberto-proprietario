from datetime import datetime, timedelta


class Sala:
    def __init__(self, nome, capacidade_maxima, recursos=None):
        self.nome = nome
        self.capacidade_maxima = capacidade_maxima
        self.recursos = recursos if recursos else []

    def __str__(self):
        return (
            f"Sala: {self.nome} | "
            f"Capacidade: {self.capacidade_maxima} | "
            f"Recursos: {', '.join(self.recursos)}"
        )


class Reserva:
    def __init__(
        self,
        solicitante,
        sala,
        data,
        horario_inicio,
        horario_termino,
        quantidade_participantes
    ):
        self.solicitante = solicitante
        self.sala = sala
        self.data = data
        self.horario_inicio = horario_inicio
        self.horario_termino = horario_termino
        self.quantidade_participantes = quantidade_participantes

    def calcular_duracao_horas(self):
        formato = "%H:%M"

        inicio = datetime.strptime(self.horario_inicio, formato)
        termino = datetime.strptime(self.horario_termino, formato)

        duracao = termino - inicio

        return duracao.total_seconds() / 3600

    def __str__(self):
        return (
            f"Solicitante: {self.solicitante} | "
            f"Sala: {self.sala.nome} | "
            f"Data: {self.data} | "
            f"Horário: {self.horario_inicio} até {self.horario_termino} | "
            f"Participantes: {self.quantidade_participantes}"
        )


class SistemaReservas:
    def __init__(self):
        self.salas = []
        self.reservas = []

    def cadastrar_sala(self, sala):
        self.salas.append(sala)

    def buscar_sala(self, nome_sala):
        for sala in self.salas:
            if sala.nome == nome_sala:
                return sala

        return None

    def horarios_conflitantes(
        self,
        inicio_novo,
        termino_novo,
        inicio_existente,
        termino_existente
    ):
        formato = "%H:%M"

        inicio_novo = datetime.strptime(inicio_novo, formato)
        termino_novo = datetime.strptime(termino_novo, formato)

        inicio_existente = datetime.strptime(inicio_existente, formato)
        termino_existente = datetime.strptime(termino_existente, formato)

        return inicio_novo < termino_existente and termino_novo > inicio_existente

    def cadastrar_reserva(
        self,
        solicitante,
        nome_sala,
        data,
        horario_inicio,
        horario_termino,
        quantidade_participantes
    ):
        sala = self.buscar_sala(nome_sala)

        if sala is None:
            print("Sala não encontrada.")
            return None

        if quantidade_participantes > sala.capacidade_maxima:
            print(
                "Reserva não permitida. "
                "Quantidade de participantes superior à capacidade da sala."
            )
            return None

        formato = "%H:%M"

        inicio = datetime.strptime(horario_inicio, formato)
        termino = datetime.strptime(horario_termino, formato)

        if termino <= inicio:
            print(
                "Reserva não permitida. "
                "O horário de término deve ser posterior ao horário de início."
            )
            return None

        for reserva in self.reservas:
            if reserva.sala.nome == nome_sala and reserva.data == data:
                if self.horarios_conflitantes(
                    horario_inicio,
                    horario_termino,
                    reserva.horario_inicio,
                    reserva.horario_termino
                ):
                    print(
                        "Reserva não permitida. "
                        "Existe conflito de horário para essa sala."
                    )
                    return None

        nova_reserva = Reserva(
            solicitante,
            sala,
            data,
            horario_inicio,
            horario_termino,
            quantidade_participantes
        )

        self.reservas.append(nova_reserva)

        print("Reserva cadastrada com sucesso.")

        return nova_reserva

    def consultar_reservas(self, nome_sala, data):
        reservas_encontradas = []

        for reserva in self.reservas:
            if reserva.sala.nome == nome_sala and reserva.data == data:
                reservas_encontradas.append(reserva)

        return reservas_encontradas

    def cancelar_reserva(
        self,
        solicitante,
        nome_sala,
        data,
        horario_inicio
    ):
        for reserva in self.reservas:
            if (
                reserva.solicitante == solicitante
                and reserva.sala.nome == nome_sala
                and reserva.data == data
                and reserva.horario_inicio == horario_inicio
            ):
                self.reservas.remove(reserva)
                print("Reserva cancelada com sucesso.")
                return True

        print("Reserva não encontrada.")
        return False

    def gerar_relatorio_horas_por_sala(self):
        relatorio = {}

        for sala in self.salas:
            relatorio[sala.nome] = 0

        for reserva in self.reservas:
            relatorio[reserva.sala.nome] += reserva.calcular_duracao_horas()

        return relatorio


# Exemplo de uso

sistema = SistemaReservas()

sala1 = Sala(
    "Sala Reunião 1",
    10,
    ["Projetor", "Televisão"]
)

sala2 = Sala(
    "Sala Reunião 2",
    20,
    ["Projetor", "Videoconferência"]
)

sistema.cadastrar_sala(sala1)
sistema.cadastrar_sala(sala2)


# Cadastro de reservas

sistema.cadastrar_reserva(
    "Patricia",
    "Sala Reunião 1",
    "20/09/2026",
    "09:00",
    "10:30",
    8
)

sistema.cadastrar_reserva(
    "Carlos",
    "Sala Reunião 1",
    "20/09/2026",
    "11:00",
    "12:00",
    5
)

sistema.cadastrar_reserva(
    "Ana",
    "Sala Reunião 2",
    "20/09/2026",
    "14:00",
    "16:00",
    15
)


# Tentativa de reserva com conflito de horário

sistema.cadastrar_reserva(
    "João",
    "Sala Reunião 1",
    "20/09/2026",
    "09:30",
    "10:00",
    4
)


# Tentativa de reserva acima da capacidade

sistema.cadastrar_reserva(
    "Maria",
    "Sala Reunião 1",
    "21/09/2026",
    "08:00",
    "09:00",
    15
)


# Consulta de reservas por sala e data

print("\nReservas da Sala Reunião 1 em 20/09/2026:")

reservas = sistema.consultar_reservas(
    "Sala Reunião 1",
    "20/09/2026"
)

for reserva in reservas:
    print(reserva)


# Cancelamento de reserva

sistema.cancelar_reserva(
    "Carlos",
    "Sala Reunião 1",
    "20/09/2026",
    "11:00"
)


# Relatório de horas reservadas por sala

print("\nRelatório de horas reservadas por sala:")

relatorio = sistema.gerar_relatorio_horas_por_sala()

for sala, horas in relatorio.items():
    print(f"{sala}: {horas:.2f} horas")