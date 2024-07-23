class Venda:
    
    # Construtor
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    # Métodos
    def toString(self, id):
        total = self.preco * self.quantidade
        print(f"Vendas #{id} - {self.nome} | {self.preco}€ x {self.quantidade} = {total:.2f}")        
