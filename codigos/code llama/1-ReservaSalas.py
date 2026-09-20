from datetime import datetime

class Sala:
    def __init__(self, nome, capacidade_maxima, recursos):
        self.nome = nome
        self.capacidade_maxima = capacidade_maxima
        self.recursos = recursos
        self.reservas = []

    def adicionar_reserva(self, reserva):
        for r in self.reservas:
            if r.data == reserva.data and not (r.horario_fim <= reserva.horario_inicio or r.horario_inicio >= reserva.horario_fim):
                print("Horário conflitante para a mesma sala.")
                return
        if reserva.quantidade_participantes > self.capacidade_maxima:
            print("Quantidade de participantes ultrapassa a capacidade da sala.")
            return
        self.reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            self.reservas.remove(reserva)

    def consultar_reservas(self, data):
        return [reserva for reserva in self.reservas if reserva.data == data]

    def gerar_relatorio(self):
        total_horas_reservadas = sum((reserva.horario_fim - reserva.horario_inicio).total_seconds() / 3600 for reserva in self.reservas)
        return total_horas_reservadas


class Reserva:
    def __init__(self, solicitante, sala, data, horario_inicio, horario_fim, quantidade_participantes):
        self.solicitante = solicitante
        self.sala = sala
        self.data = datetime.strptime(data, '%Y-%m-%d')
        self.horario_inicio = datetime.strptime(horario_inicio, '%H:%M')
        self.horario_fim = datetime.strptime(horario_fim, '%H:%M')
        self.quantidade_participantes = quantidade_participantes


class Sistema:
    def __init__(self):
        self.salas = []

    def adicionar_sala(self, sala):
        self.salas.append(sala)

    def consultar_sala(self, nome_sala):
        for sala in self.salas:
            if sala.nome == nome_sala:
                return sala
        return None


# Exemplo de uso
sistema = Sistema()

sala1 = Sala('Sala 1', 10, ['projetor', 'televisão'])
sala2 = Sala('Sala 2', 20, ['videoconferência'])

sistema.adicionar_sala(sala1)
sistema.adicionar_sala(sala2)

reserva1 = Reserva('Solicitante 1', sala1, '2024-09-20', '09:00', '11:00', 5)
reserva2 = Reserva('Solicitante 2', sala1, '2024-09-20', '11:00', '13:00', 8)
reserva3 = Reserva('Solicitante 3', sala2, '2024-09-21', '09:00', '12:00', 15)

sala1.adicionar_reserva(reserva1)
sala1.adicionar_reserva(reserva2)
sala2.adicionar_reserva(reserva3)

print("Reservas da Sala 1 em 2024-09-20:")
for reserva in sala1.consultar_reservas(datetime.strptime('2024-09-20', '%Y-%m-%d')):
    print(f"Solicitante: {reserva.solicitante}, Horário: {reserva.horario_inicio.strftime('%H:%M')} - {reserva.horario_fim.strftime('%H:%M')}")

print(f"Total de horas reservadas na Sala 1: {sala1.gerar_relatorio()}")
print(f"Total de horas reservadas na Sala 2: {sala2.gerar_relatorio()}")