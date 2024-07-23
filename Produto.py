class Produto:
    
    # Construtor
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    # Métodos
    def toString(self, id):
        print(f"#{id + 1} - Nome: {self.nome:<12} | Preço: {self.preco:<6.2f}€ | Quantidade: {self.quantidade}")
        
    def nomeEIgual(self, nome_verificar):
        if(nome_verificar.lower() == self.nome.lower()): return True
        else: return False
        
    def setNome(self, novo_nome):
        self.nome = novo_nome
        
    def setPreco(self, novo_preco):
        self.preco = novo_preco
        
    def setQuant(self, nova_quant):
        self.quantidade = nova_quant
        
    def setQuant2(self, quant_vendida):
        self.quantidade -= quant_vendida
        

