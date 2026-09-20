class Fornecedor:
    def __init__(self, nome, prazo_entrega, preco):
        self.nome = nome
        self.prazo_entrega = prazo_entrega
        self.preco = preco

    def __str__(self):
        return (
            f"{self.nome} | "
            f"Prazo: {self.prazo_entrega} dias | "
            f"Preço: R$ {self.preco:.2f}"
        )


class Produto:
    def __init__(
        self,
        codigo,
        nome,
        categoria,
        quantidade_atual,
        quantidade_minima,
        fornecedores=None
    ):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.quantidade_atual = quantidade_atual
        self.quantidade_minima = quantidade_minima
        self.fornecedores = fornecedores if fornecedores else []

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)

    def registrar_entrada(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade de entrada deve ser maior que zero.")

        self.quantidade_atual += quantidade

    def registrar_saida(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade de saída deve ser maior que zero.")

        if quantidade > self.quantidade_atual:
            raise ValueError(
                f"Estoque insuficiente. Quantidade disponível: "
                f"{self.quantidade_atual}"
            )

        self.quantidade_atual -= quantidade

    def precisa_reposicao(self):
        return self.quantidade_atual < self.quantidade_minima

    def fornecedor_recomendado(self):
        if not self.fornecedores:
            return None

        # Primeiro considera o menor preço.
        # Em caso de empate, escolhe o menor prazo.
        return min(
            self.fornecedores,
            key=lambda fornecedor: (
                fornecedor.preco,
                fornecedor.prazo_entrega
            )
        )

    def valor_estimado(self):
        """
        Calcula o valor estimado do estoque com base no menor preço
        disponível entre os fornecedores.
        """

        fornecedor = self.fornecedor_recomendado()

        if fornecedor is None:
            return 0

        return self.quantidade_atual * fornecedor.preco

    def __str__(self):
        return (
            f"Código: {self.codigo} | "
            f"Nome: {self.nome} | "
            f"Categoria: {self.categoria} | "
            f"Quantidade: {self.quantidade_atual} | "
            f"Mínimo: {self.quantidade_minima}"
        )


class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        if produto.codigo in self.produtos:
            raise ValueError("Já existe um produto com esse código.")

        self.produtos[produto.codigo] = produto

    def buscar_produto(self, codigo):
        return self.produtos.get(codigo)

    def registrar_entrada(self, codigo, quantidade):
        produto = self.buscar_produto(codigo)

        if produto is None:
            raise ValueError("Produto não encontrado.")

        produto.registrar_entrada(quantidade)

        print(
            f"Entrada de {quantidade} unidade(s) de "
            f"{produto.nome} registrada com sucesso."
        )

    def registrar_saida(self, codigo, quantidade):
        produto = self.buscar_produto(codigo)

        if produto is None:
            raise ValueError("Produto não encontrado.")

        produto.registrar_saida(quantidade)

        print(
            f"Saída de {quantidade} unidade(s) de "
            f"{produto.nome} registrada com sucesso."
        )

        if produto.precisa_reposicao():
            print(
                f"ATENÇÃO: {produto.nome} está abaixo "
                f"do estoque mínimo."
            )

            fornecedor = produto.fornecedor_recomendado()

            if fornecedor:
                print(
                    f"Fornecedor recomendado: {fornecedor.nome} | "
                    f"Preço: R$ {fornecedor.preco:.2f} | "
                    f"Prazo: {fornecedor.prazo_entrega} dias"
                )

    def consultar_por_categoria(self, categoria):
        produtos_encontrados = []

        for produto in self.produtos.values():
            if produto.categoria.lower() == categoria.lower():
                produtos_encontrados.append(produto)

        return produtos_encontrados

    def produtos_abaixo_minimo(self):
        return [
            produto
            for produto in self.produtos.values()
            if produto.precisa_reposicao()
        ]

    def valor_total_estimado_estoque(self):
        total = 0

        for produto in self.produtos.values():
            total += produto.valor_estimado()

        return total

    def gerar_relatorio(self):
        print("\n" + "=" * 60)
        print("RELATÓRIO DE ESTOQUE")
        print("=" * 60)

        produtos_abaixo = self.produtos_abaixo_minimo()

        print("\nPRODUTOS ABAIXO DO ESTOQUE MÍNIMO")

        if not produtos_abaixo:
            print("Nenhum produto necessita de reposição.")

        else:
            for produto in produtos_abaixo:
                print("\n" + "-" * 40)
                print(f"Código: {produto.codigo}")
                print(f"Produto: {produto.nome}")
                print(f"Categoria: {produto.categoria}")
                print(
                    f"Quantidade atual: {produto.quantidade_atual}"
                )
                print(
                    f"Quantidade mínima: {produto.quantidade_minima}"
                )

                fornecedor = produto.fornecedor_recomendado()

                if fornecedor:
                    print("Fornecedor recomendado:")
                    print(f"  Nome: {fornecedor.nome}")
                    print(
                        f"  Preço: R$ {fornecedor.preco:.2f}"
                    )
                    print(
                        f"  Prazo: {fornecedor.prazo_entrega} dias"
                    )
                else:
                    print("Nenhum fornecedor cadastrado.")

        print("\n" + "-" * 60)

        valor_total = self.valor_total_estimado_estoque()

        print(
            f"Valor total estimado do estoque: "
            f"R$ {valor_total:.2f}"
        )

        print("=" * 60)


# ---------------------------------------------------------
# EXEMPLO DE UTILIZAÇÃO
# ---------------------------------------------------------

if __name__ == "__main__":

    estoque = Estoque()

    # Fornecedores do produto 1
    fornecedor1 = Fornecedor(
        nome="Fornecedor A",
        prazo_entrega=5,
        preco=10.00
    )

    fornecedor2 = Fornecedor(
        nome="Fornecedor B",
        prazo_entrega=3,
        preco=10.00
    )

    fornecedor3 = Fornecedor(
        nome="Fornecedor C",
        prazo_entrega=2,
        preco=12.00
    )

    # Produto 1
    produto1 = Produto(
        codigo=1,
        nome="Caneta Azul",
        categoria="Papelaria",
        quantidade_atual=20,
        quantidade_minima=10
    )

    produto1.adicionar_fornecedor(fornecedor1)
    produto1.adicionar_fornecedor(fornecedor2)
    produto1.adicionar_fornecedor(fornecedor3)

    # Fornecedores do produto 2
    fornecedor4 = Fornecedor(
        nome="Fornecedor D",
        prazo_entrega=7,
        preco=25.00
    )

    fornecedor5 = Fornecedor(
        nome="Fornecedor E",
        prazo_entrega=4,
        preco=27.00
    )

    # Produto 2
    produto2 = Produto(
        codigo=2,
        nome="Caderno Universitário",
        categoria="Papelaria",
        quantidade_atual=8,
        quantidade_minima=15
    )

    produto2.adicionar_fornecedor(fornecedor4)
    produto2.adicionar_fornecedor(fornecedor5)

    # Produto 3
    fornecedor6 = Fornecedor(
        nome="Fornecedor F",
        prazo_entrega=10,
        preco=150.00
    )

    produto3 = Produto(
        codigo=3,
        nome="Teclado",
        categoria="Informática",
        quantidade_atual=5,
        quantidade_minima=3
    )

    produto3.adicionar_fornecedor(fornecedor6)

    # Adicionando produtos ao estoque
    estoque.adicionar_produto(produto1)
    estoque.adicionar_produto(produto2)
    estoque.adicionar_produto(produto3)

    # -----------------------------------------------------
    # Entrada de produto
    # -----------------------------------------------------

    try:
        estoque.registrar_entrada(1, 5)
    except ValueError as erro:
        print("Erro:", erro)

    # -----------------------------------------------------
    # Saída de produto
    # -----------------------------------------------------

    try:
        estoque.registrar_saida(1, 18)
    except ValueError as erro:
        print("Erro:", erro)

    # Teste de saída maior que o estoque
    try:
        estoque.registrar_saida(3, 20)
    except ValueError as erro:
        print("Erro:", erro)

    # -----------------------------------------------------
    # Consulta por categoria
    # -----------------------------------------------------

    print("\nPRODUTOS DA CATEGORIA PAPELARIA")

    produtos_papelaria = estoque.consultar_por_categoria(
        "Papelaria"
    )

    for produto in produtos_papelaria:
        print(produto)

    # -----------------------------------------------------
    # Relatório
    # -----------------------------------------------------

    estoque.gerar_relatorio()