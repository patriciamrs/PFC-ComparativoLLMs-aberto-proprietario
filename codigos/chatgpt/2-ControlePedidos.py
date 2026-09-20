class ItemPedido:
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def calcular_total(self):
        return self.quantidade * self.preco_unitario


class Pedido:
    CUPONS_VALIDOS = {
        "DESCONTO10",
        "CLIENTE10",
        "PROMO10"
    }

    def __init__(
        self,
        numero,
        nome_cliente,
        tipo_atendimento,
        distancia_km=0,
        cupom=None
    ):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.tipo_atendimento = tipo_atendimento
        self.distancia_km = distancia_km
        self.cupom = cupom
        self.itens = []

    def adicionar_item(self, nome, quantidade, preco_unitario):
        for item in self.itens:
            if item.nome == nome:
                item.quantidade += quantidade
                return

        novo_item = ItemPedido(
            nome,
            quantidade,
            preco_unitario
        )

        self.itens.append(novo_item)

    def remover_item(self, nome):
        for item in self.itens:
            if item.nome == nome:
                self.itens.remove(item)
                return True

        return False

    def alterar_quantidade(self, nome, nova_quantidade):
        for item in self.itens:
            if item.nome == nome:
                if nova_quantidade <= 0:
                    self.itens.remove(item)
                else:
                    item.quantidade = nova_quantidade

                return True

        return False

    def calcular_subtotal(self):
        subtotal = 0

        for item in self.itens:
            subtotal += item.calcular_total()

        return subtotal

    def calcular_desconto_acima_100(self):
        subtotal = self.calcular_subtotal()

        if subtotal > 100:
            return subtotal * 0.05

        return 0

    def cupom_valido(self):
        return self.cupom in self.CUPONS_VALIDOS

    def calcular_desconto_cupom(self):
        subtotal = self.calcular_subtotal()

        if self.cupom_valido():
            return subtotal * 0.10

        return 0

    def calcular_taxa_entrega(self):
        if self.tipo_atendimento.lower() == "retirada":
            return 0

        if self.tipo_atendimento.lower() != "entrega":
            return 0

        if self.distancia_km <= 3:
            return 5.00

        if self.distancia_km <= 7:
            return 8.00

        if self.distancia_km <= 12:
            return 12.00

        return 15.00

    def calcular_resumo(self):
        subtotal = self.calcular_subtotal()

        desconto_acima_100 = self.calcular_desconto_acima_100()
        desconto_cupom = self.calcular_desconto_cupom()

        total_descontos = (
            desconto_acima_100
            + desconto_cupom
        )

        taxa_entrega = self.calcular_taxa_entrega()

        valor_final = (
            subtotal
            - total_descontos
            + taxa_entrega
        )

        return {
            "subtotal": subtotal,
            "desconto_acima_100": desconto_acima_100,
            "desconto_cupom": desconto_cupom,
            "total_descontos": total_descontos,
            "taxa_entrega": taxa_entrega,
            "valor_final": valor_final
        }

    def exibir_resumo(self):
        resumo = self.calcular_resumo()

        print(f"\nPedido: {self.numero}")
        print(f"Cliente: {self.nome_cliente}")
        print(f"Tipo de atendimento: {self.tipo_atendimento}")

        print("\nItens:")

        for item in self.itens:
            print(
                f"{item.nome} - "
                f"{item.quantidade} x "
                f"R$ {item.preco_unitario:.2f} = "
                f"R$ {item.calcular_total():.2f}"
            )

        print(f"\nSubtotal: R$ {resumo['subtotal']:.2f}")

        print(
            "Desconto pedido acima de R$ 100,00: "
            f"R$ {resumo['desconto_acima_100']:.2f}"
        )

        print(
            "Desconto por cupom: "
            f"R$ {resumo['desconto_cupom']:.2f}"
        )

        print(
            "Total de descontos: "
            f"R$ {resumo['total_descontos']:.2f}"
        )

        print(
            "Taxa de entrega: "
            f"R$ {resumo['taxa_entrega']:.2f}"
        )

        print(
            "Valor final: "
            f"R$ {resumo['valor_final']:.2f}"
        )


class SistemaRestaurante:
    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def consultar_pedidos_cliente(self, nome_cliente):
        pedidos_cliente = []

        for pedido in self.pedidos:
            if pedido.nome_cliente.lower() == nome_cliente.lower():
                pedidos_cliente.append(pedido)

        return pedidos_cliente

    def buscar_pedido(self, numero):
        for pedido in self.pedidos:
            if pedido.numero == numero:
                return pedido

        return None


# Exemplo de uso

sistema = SistemaRestaurante()


pedido1 = Pedido(
    numero=1,
    nome_cliente="Patricia",
    tipo_atendimento="entrega",
    distancia_km=5,
    cupom="DESCONTO10"
)

pedido1.adicionar_item(
    "Pizza Grande",
    1,
    75.00
)

pedido1.adicionar_item(
    "Refrigerante",
    2,
    10.00
)

pedido1.adicionar_item(
    "Sobremesa",
    1,
    20.00
)

sistema.adicionar_pedido(pedido1)


pedido2 = Pedido(
    numero=2,
    nome_cliente="Carlos",
    tipo_atendimento="retirada"
)

pedido2.adicionar_item(
    "Hambúrguer",
    2,
    25.00
)

pedido2.adicionar_item(
    "Batata Frita",
    1,
    15.00
)

sistema.adicionar_pedido(pedido2)


pedido3 = Pedido(
    numero=3,
    nome_cliente="Patricia",
    tipo_atendimento="retirada"
)

pedido3.adicionar_item(
    "Lasanha",
    1,
    45.00
)

sistema.adicionar_pedido(pedido3)


# Alterando quantidade de um item

pedido1.alterar_quantidade(
    "Refrigerante",
    3
)


# Removendo um item

pedido2.remover_item(
    "Batata Frita"
)


# Exibindo resumo do primeiro pedido

pedido1.exibir_resumo()


# Consultando pedidos de determinado cliente

print("\nPedidos realizados por Patricia:")

pedidos_patricia = sistema.consultar_pedidos_cliente(
    "Patricia"
)

for pedido in pedidos_patricia:
    print(
        f"Pedido {pedido.numero} - "
        f"Valor final: "
        f"R$ {pedido.calcular_resumo()['valor_final']:.2f}"
    )