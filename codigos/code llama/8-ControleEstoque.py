class Fornecedor:
    def __init__(self, nome, prazo_medio_entrega, preco):
        self.nome = nome
        self.prazo_medio_entrega = prazo_medio_entrega
        self.preco = preco

class Produto:
    def __init__(self, codigo, nome, categoria, quantidade_atual, quantidade_minima):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.quantidade_atual = quantidade_atual
        self.quantidade_minima = quantidade_minima
        self.fornecedores = []

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)

    def registrar_entrada(self, quantidade):
        self.quantidade_atual += quantidade

    def registrar_saida(self, quantidade):
        if quantidade > self.quantidade_atual:
            print("Saída superior à quantidade disponível em estoque.")
            return
        self.quantidade_atual -= quantidade

    def verificar_estoque(self):
        if self.quantidade_atual < self.quantidade_minima:
            return True
        return False

    def selecionar_fornecedor(self):
        if not self.fornecedores:
            return None
        fornecedor_selecionado = min(self.fornecedores, key=lambda x: (x.preco, x.prazo_medio_entrega))
        return fornecedor_selecionado

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def consultar_produtos_por_categoria(self, categoria):
        return [produto for produto in self.produtos if produto.categoria == categoria]

    def gerar_relatorio(self):
        relatorio = []
        valor_total_estimado = 0
        for produto in self.produtos:
            if produto.verificar_estoque():
                fornecedor_selecionado = produto.selecionar_fornecedor()
                if fornecedor_selecionado:
                    relatorio.append({
                        "produto": produto.nome,
                        "fornecedor_recomendado": fornecedor_selecionado.nome,
                        "preco": fornecedor_selecionado.preco,
                        "prazo_medio_entrega": fornecedor_selecionado.prazo_medio_entrega
                    })
            valor_total_estimado += produto.quantidade_atual * produto.fornecedores[0].preco if produto.fornecedores else 0
        return relatorio, valor_total_estimado

# Exemplo de uso
estoque = Estoque()

produto1 = Produto("001", "Produto 1", "Categoria 1", 10, 5)
fornecedor1 = Fornecedor("Fornecedor 1", 3, 10.0)
fornecedor2 = Fornecedor("Fornecedor 2", 2, 9.0)
produto1.adicionar_fornecedor(fornecedor1)
produto1.adicionar_fornecedor(fornecedor2)

produto2 = Produto("002", "Produto 2", "Categoria 2", 20, 10)
fornecedor3 = Fornecedor("Fornecedor 3", 4, 15.0)
produto2.adicionar_fornecedor(fornecedor3)

estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)

print(estoque.consultar_produtos_por_categoria("Categoria 1"))
relatorio, valor_total_estimado = estoque.gerar_relatorio()
print(relatorio)
print(valor_total_estimado)