print("\n\n")

from funcoes import*

limpar()

inicial()

while(True):
    
    opcao = menu()
    
    limpar()
    
    if(opcao == 1): registar_produto()
    elif(opcao == 2): editar_produto()
    elif(opcao == 3): apagar_produto()
    elif(opcao == 4): listar_produto(True)
    elif(opcao == 5): vender_produto()
    elif(opcao == 6): listar_vendas()
    
    elif(opcao == 0):
        animacao("A Sair")
        break
    
    else: print("--- OPÇÃO INVÁLIDA! ---")
    
    carregueEnter()
    

    

print("\n\n")