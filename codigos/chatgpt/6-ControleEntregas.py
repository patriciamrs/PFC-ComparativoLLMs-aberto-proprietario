from datetime import date


class Entrega:
    STATUS_VALIDOS = [
        "aguardando coleta",
        "em transporte",
        "entregue",
        "cancelada"
    ]

    def __init__(
        self,
        codigo,
        cliente,
        endereco_origem,
        endereco_destino,
        peso,
        distancia,
        data_prevista
    ):
        self.codigo = codigo
        self.cliente = cliente
        self.endereco_origem = endereco_origem
        self.endereco_destino = endereco_destino
        self.peso = peso
        self.distancia = distancia
        self.data_prevista = data_prevista
        self.status = "aguardando coleta"
        self.atrasada = False

    def calcular_preco(self):
        valor_base = 10.00

        valor_peso = self.peso * 2.00
        valor_distancia = self.distancia * 0.50

        total = valor_base + valor_peso + valor_distancia

        if self.peso > 20:
            total += 25.00

        if self.distancia > 200:
            total += 40.00

        return total

    def atualizar_status(self, novo_status):
        if self.status == "cancelada":
            print("Não é possível alterar uma entrega cancelada.")
            return False

        if novo_status not in self.STATUS_VALIDOS:
            print("Status inválido.")
            return False

        self.status = novo_status

        return True

    def verificar_atraso(self):
        if self.status not in ["entregue", "cancelada"]:
            if date.today() > self.data_prevista:
                self.atrasada = True
            else:
                self.atrasada = False

        return self.atrasada

    def __str__(self):
        return (
            f"Código: {self.codigo} | "
            f"Cliente: {self.cliente} | "
            f"Status: {self.status} | "
            f"Peso: {self.peso} kg | "
            f"Distância: {self.distancia} km | "
            f"Preço: R$ {self.calcular_preco():.2f} | "
            f"Atrasada: {'Sim' if self.verificar_atraso() else 'Não'}"
        )


class SistemaTransportadora:
    def __init__(self):
        self.entregas = []

    def cadastrar_entrega(
        self,
        codigo,
        cliente,
        endereco_origem,
        endereco_destino,
        peso,
        distancia,
        data_prevista
    ):
        if self.buscar_entrega(codigo):
            print("Já existe uma entrega com esse código.")
            return None

        entrega = Entrega(
            codigo,
            cliente,
            endereco_origem,
            endereco_destino,
            peso,
            distancia,
            data_prevista
        )

        self.entregas.append(entrega)

        print("Entrega cadastrada com sucesso.")

        return entrega

    def buscar_entrega(self, codigo):
        for entrega in self.entregas:
            if entrega.codigo == codigo:
                return entrega

        return None

    def atualizar_status(self, codigo, novo_status):
        entrega = self.buscar_entrega(codigo)

        if entrega is None:
            print("Entrega não encontrada.")
            return False

        if entrega.atualizar_status(novo_status):
            print("Status atualizado com sucesso.")
            return True

        return False

    def consultar_por_cliente(self, cliente):
        return [
            entrega
            for entrega in self.entregas
            if entrega.cliente.lower() == cliente.lower()
        ]

    def listar_entregas_atrasadas(self):
        atrasadas = []

        for entrega in self.entregas:
            if entrega.verificar_atraso():
                atrasadas.append(entrega)

        return atrasadas

    def gerar_relatorio(self):
        quantidade_status = {
            "aguardando coleta": 0,
            "em transporte": 0,
            "entregue": 0,
            "cancelada": 0
        }

        valor_total = 0

        for entrega in self.entregas:
            quantidade_status[entrega.status] += 1

            if entrega.status != "cancelada":
                valor_total += entrega.calcular_preco()

        return {
            "valor_total": valor_total,
            "quantidade_status": quantidade_status
        }


# Exemplo de uso

sistema = SistemaTransportadora()


# Cadastro das entregas

sistema.cadastrar_entrega(
    "E001",
    "Patricia",
    "Criciúma - SC",
    "Florianópolis - SC",
    10,
    200,
    date(2026, 9, 25)
)

sistema.cadastrar_entrega(
    "E002",
    "Carlos",
    "Criciúma - SC",
    "Curitiba - PR",
    25,
    500,
    date(2026, 9, 18)
)

sistema.cadastrar_entrega(
    "E003",
    "Patricia",
    "Criciúma - SC",
    "Tubarão - SC",
    5,
    70,
    date(2026, 9, 23)
)


# Atualização de status

sistema.atualizar_status(
    "E001",
    "em transporte"
)

sistema.atualizar_status(
    "E002",
    "em transporte"
)

sistema.atualizar_status(
    "E003",
    "cancelada"
)


# Tentativa de alterar uma entrega cancelada

sistema.atualizar_status(
    "E003",
    "entregue"
)


# Consulta por cliente

print("\nEntregas da Patricia:")

entregas_cliente = sistema.consultar_por_cliente(
    "Patricia"
)

for entrega in entregas_cliente:
    print(entrega)


# Entregas atrasadas

print("\nEntregas atrasadas:")

for entrega in sistema.listar_entregas_atrasadas():
    print(entrega)


# Relatório

relatorio = sistema.gerar_relatorio()

print("\nRelatório geral:")

print(
    f"Valor total das entregas: "
    f"R$ {relatorio['valor_total']:.2f}"
)

print("\nQuantidade por status:")

for status, quantidade in relatorio["quantidade_status"].items():
    print(
        f"{status}: {quantidade}"
    )