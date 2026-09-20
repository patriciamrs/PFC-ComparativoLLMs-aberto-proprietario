from datetime import datetime

class Entrega:
    def __init__(self, codigo, cliente, origem, destino, peso, distancia, data_prevista):
        self.codigo = codigo
        self.cliente = cliente
        self.origem = origem
        self.destino = destino
        self.peso = peso
        self.distancia = distancia
        self.data_prevista = datetime.strptime(data_prevista, '%Y-%m-%d')
        self.status = 'aguardando coleta'
        self.atraso = False

    def calcular_preco(self):
        preco_base = self.peso * 0.5 + self.distancia * 0.1
        if self.peso > 20:
            preco_base += 5
        if self.distancia > 200:
            preco_base += 10
        return preco_base

    def atualizar_status(self, novo_status):
        if self.status == 'cancelada':
            print('Entrega cancelada não pode ser alterada.')
            return
        self.status = novo_status
        if novo_status == 'entregue' and datetime.today() > self.data_prevista:
            self.atraso = True

    def registrar_atraso(self):
        if self.status == 'entregue' and datetime.today() > self.data_prevista:
            self.atraso = True


class Sistema:
    def __init__(self):
        self.entregas = []

    def adicionar_entrega(self, entrega):
        self.entregas.append(entrega)

    def consultar_entregas_por_cliente(self, cliente):
        return [entrega for entrega in self.entregas if entrega.cliente == cliente]

    def gerar_relatorio(self):
        valor_total = sum(entrega.calcular_preco() for entrega in self.entregas)
        status_contagem = {'aguardando coleta': 0, 'em transporte': 0, 'entregue': 0, 'cancelada': 0}
        for entrega in self.entregas:
            status_contagem[entrega.status] += 1
        return valor_total, status_contagem


# Exemplo de uso
sistema = Sistema()

entrega1 = Entrega('001', 'Cliente 1', 'Origem 1', 'Destino 1', 15, 150, '2024-09-20')
entrega2 = Entrega('002', 'Cliente 2', 'Origem 2', 'Destino 2', 25, 250, '2024-09-25')

sistema.adicionar_entrega(entrega1)
sistema.adicionar_entrega(entrega2)

entrega1.atualizar_status('em transporte')
entrega2.atualizar_status('entregue')

print(f'Preço da entrega 1: {entrega1.calcular_preco()}')
print(f'Preço da entrega 2: {entrega2.calcular_preco()}')

entregas_cliente1 = sistema.consultar_entregas_por_cliente('Cliente 1')
print(f'Entregas do cliente 1: {[entrega.codigo for entrega in entregas_cliente1]}')

valor_total, status_contagem = sistema.gerar_relatorio()
print(f'Valor total das entregas: {valor_total}')
print(f'Contagem de status: {status_contagem}')