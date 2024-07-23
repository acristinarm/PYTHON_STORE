import time
import os
import globais
from Produto import *
from Venda import *

# Funções Auxiliares
def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguardar(tempo):
    time.sleep(tempo)

def animacao(frase):
    tempo = 0.3
    limpar()
    print(frase, end="", flush=True)
    aguardar(tempo)
    for i in range(3):
        print(".", end="", flush=True)
        aguardar(tempo)
    limpar()
    
def carregueEnter():
    input("\nCarregue <ENTER> para continuar")
    animacao("Aguarde")
    limpar()
    
# Funções Helpers

def inicial():
    globais.produtos.append(Produto('Caneta Azul', 1.25, 20))
    globais.produtos.append(Produto('Caderno A4', 3.99, 12))    
    globais.produtos.append(Produto('Mesa', 49.99, 6))    

def verificar_existencia(nome_verificar):
    for produto in globais.produtos:
        if(produto.nomeEIgual(nome_verificar)): return True
    return False

# Funções Principais

def menu():
    print("=== Loja Python === \n")
    print("1 - Registar Produto")
    print("2 - Editar Produto")
    print("3 - Apagar Produto")
    print("4 - Listar Produto \n")
    print("5 - Vender")
    print("6 - Listar Vendas \n")
    print("0 - Sair \n")
    return int(input("- Opção: "))

def registar_produto():
    print("--- Registar Produto --- \n")
    nome = input("- Digite o nome do novo produto: ")
    if(verificar_existencia(nome) == False):
        preco = float(input("- Digite o preço deste produto: "))
        quantidade = int(input("- Digite a quantidade deste produto: "))
        globais.produtos.append(Produto(nome, preco, quantidade))
        print("\n--- SUCESSO! ---")
    else:
        print("\n--- ERRO! ESSE PRODUTO JÁ EXISTE! ---")
        
def editar_produto():
    print("--- Editar Produto --- \n")
    listar_produto(False)
    id = int(input("\n- Digite o Id do produto que deseja editar: ")) -1
    if (id >= 0 and id < len(globais.produtos)):
        print()
        produto = globais.produtos[id]
        produto.toString(id)
        
        print("\n--- Menu de Edição --- \n")
        print("1 - Nome")
        print("2 - Preço")
        print("3 - Quantidade \n")
        print("0 - Cancelar \n")
        opcao = int(input("- Opção: "))
        
        if(opcao == 1):
            novo_nome = input(f"\n- Digite o nome para substituir ({produto.nome}): ")
            if(verificar_existencia(novo_nome) == False):
                produto.setNome(novo_nome)
                print("\n--- SUCESSO! ---")
            else: print("\n--- ERRO! ESSE PRODUTO JÁ EXISTE! ---")
        elif(opcao == 2):
            novo_preco = float(input(f"\n- Digite o preço que vai substituir ({produto.preco}): "))
            if(novo_preco > 0):
                produto.setPreco(novo_preco)
                print("\n--- SUCESSO! ---")
            else: print("\n--- ERRO! DIGITE UM VALOR VÁLIDO! ---")
        elif(opcao == 3):
            nova_quant = int(input(f"\n- Digite a quantidade que vai substituir ({produto.quantidade}): "))
            if(nova_quant >= 0):
                produto.setQuant(nova_quant)
                print("\n--- SUCESSO! ---")
            else: print("\n--- ERRO! DIGITE UM VALOR VÁLIDO! ---")
        elif(opcao == 0):
            print("\n OPERAÇÃO CANCELADA")
        else:
            print("\n--- DIGITE UMA OPÇÃO VÁLIDA ---")  
    else:
        print("\n--- OPÇÃO INVÁLIDA ---")

def apagar_produto():
    print("--- Apagar Produto --- \n")
    listar_produto(False)
    id = int(input("\n- Digite o Id do produto que deseja apagar: ")) -1
    if(id >= 0 and id < len(globais.produtos)):
        print("\n--- SUCESSO! ---")
        globais.produtos.pop(id)
    else: print("\n--- ERRO! DIGITE UM ID VÁLIDO! ---")

def listar_produto(com_titulo):
    if(com_titulo): print("--- Lista de Produtos --- \n")
        
    id = 0  
    for produto in globais.produtos:
        produto.toString(id)
        id += 1
        
def vender_produto():
    print("--- Vender Produto --- \n")
    listar_produto(False)
    id = int(input("\n- Digite o Id do produto que deseja vender: ")) -1
    if(id >= 0 and id < len(globais.produtos)):
        produto = globais.produtos[id]
        quant_vendida = int(input(f"\n- Digite a quantidade de ({produto.nome}) que será vendida: "))
        if(quant_vendida > 0 and quant_vendida <= produto.quantidade):
            venda = Venda(produto.nome, produto.preco, quant_vendida)
            globais.vendas.append(venda)
            produto.setQuant2(quant_vendida)
            print()
            venda.toString(len(globais.vendas))  
        else: print("\n--- QUANTIDADE INVÁLIDA! ---")
    else: print("\n--- ERRO! DIGITE UM ID VÁLIDO! ---")

def listar_vendas():
    print("--- Lista de Vendas --- \n")
    id = 1
    total = 0
    for venda in globais.vendas:
        venda.toString(id)
        id += 1
        total += venda.preco * venda.quantidade
    print(f"\nValor total das vendas : {total:.2f}")
    
    print