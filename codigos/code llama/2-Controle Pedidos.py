class Item:
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

class Pedido:
    def __init__(self, numero, nome_cliente, tipo_atendimento):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.tipo_atendimento = tipo_atendimento
        self.itens = []
        self.cupom = None
        self.distancia = None

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)

    def alterar_quantidade(self, item, nova_quantidade):
        if item in self.itens:
            item.quantidade = nova_quantidade

    def calcular_subtotal(self):
        return sum(item.quantidade * item.preco_unitario for item in self.itens)

    def calcular_desconto(self):
        subtotal = self.calcular_subtotal()
        desconto = 0
        if subtotal > 100:
            desconto += subtotal * 0.05
        if self.cupom:
            desconto += subtotal * 0.10
        return desconto

    def calcular_taxa_entrega(self):
        if self.tipo_atendimento == 'entrega':
            if self.distancia:
                return self.distancia * 0.5
            else:
                return 0
        else:
            return 0

    def calcular_valor_final(self):
        subtotal = self.calcular_subtotal()
        desconto = self.calcular_desconto()
        taxa_entrega = self.calcular_taxa_entrega()
        return subtotal - desconto + taxa_entrega

class Sistema:
    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def consultar_pedidos_por_cliente(self, nome_cliente):
        return [pedido for pedido in self.pedidos if pedido.nome_cliente == nome_cliente]

    def gerar_resumo(self, pedido):
        subtotal = pedido.calcular_subtotal()
        descontos = pedido.calcular_desconto()
        taxa_entrega = pedido.calcular_taxa_entrega()
        valor_final = pedido.calcular_valor_final()
        return {
            'subtotal': subtotal,
            'descontos': descontos,
            'taxa_entrega': taxa_entrega,
            'valor_final': valor_final
        }


# Exemplo de uso
sistema = Sistema()

pedido1 = Pedido('001', 'Cliente 1', 'retirada')
pedido2 = Pedido('002', 'Cliente 2', 'entrega')

sistema.adicionar_pedido(pedido1)
sistema.adicionar_pedido(pedido2)

item1 = Item('Item 1', 2, 20.0)
item2 = Item('Item 2', 3, 30.0)

pedido1.adicionar_item(item1)
pedido1.adicionar_item(item2)

pedido2.distancia = 5

resumo_pedido1 = sistema.gerar_resumo(pedido1)
resumo_pedido2 = sistema.gerar_resumo(pedido2)

print(f'Pedido 1 - Subtotal: {resumo_pedido1["subtotal"]}, Descontos: {resumo_pedido1["descontos"]}, Taxa Entrega: {resumo_pedido1["taxa_entrega"]}, Valor Final: {resumo_pedido1["valor_final"]}')
print(f'Pedido 2 - Subtotal: {resumo_pedido2["subtotal"]}, Descontos: {resumo_pedido2["descontos"]}, Taxa Entrega: {resumo_pedido2["taxa_entrega"]}, Valor Final: {resumo_pedido2["valor_final"]}')