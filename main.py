from class_computador import Computador
from class_desktop import Desktop
from class_notebook import Notebook

while True:
    escolha = input("Deseja criar 1 - Desktop | 2 - Notebook  => ")     
    if escolha == "1":
        marca_desktop = input("\nDigite a marca do computador => ")
        cor_desktop = input("\nDigite a cor do desktop => ")
        preco_desktop = int(input("\nDigite o valor do desktop =>"))
        fonte_desktop = int(input("\nDigite a potencia da fonte do desktop => "))
        desktop = Desktop(marca_desktop, cor_desktop, preco_desktop, fonte_desktop)
        print(desktop.getInformacoes())
        desktop.cadastrar()

    if escolha == "2":
        marca_notebook = input("\nDigite a marca do computador => ")
        cor_notebook = input("\nDigite a cor do notebook => ")
        preco_notebook = int(input("\nDigite o valor do notebook =>"))
        tempo_notebook = int(input("\nDigite o tempo de bateria, em horas, do notebook => "))
        notebook = Notebook(marca_notebook, cor_notebook, preco_notebook, tempo_notebook)
        print(notebook.getInformacoes())
        notebook.cadastrar()
    
    if not escolha:
        print("Saindo")
        break
