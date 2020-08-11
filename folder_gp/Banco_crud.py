import os
import time

def carregar_cliente():
    lista = []

    try:
        arquivo = open("banco_movimentacao.txt", "r")

        for linha in arquivo.readlines(): #armazena em linha a o valor da linha
            coluna = linha.strip().split("#") #coluna recebe agora um vetor
            cliente = {
                "cpf": coluna[1],
                "nome": coluna[0],
                "agencia": coluna[2],
                "conta": coluna[3],
                "senha": coluna[4]
            }
            lista.append(cliente)

        arquivo.close()
    except FileNotFoundError:
        print("Arquivo não existe - Criar....")
        pass

    return lista

def salvar_cliente(lista):

    arquivo = open("banco_movimentacao.txt", "w")#se não existir arquivo cria um novo

    for cliente in lista:
        arquivo.write('{}#{}#{}#{}#{}\n'.format(cliente['nome'], cliente['cpf'], cliente['agencia'], cliente['conta'], cliente['senha']))
    arquivo.close()
    print(".")
    print(".")
    print(".")
    time.sleep(2)
    from folder_gp_1.Main import Proj
    main = Proj()
    main.init()
    os.system("cls")
    
    
def adicionar(lista):
    cliente = {
        "cpf": input("Digite o cpf: "),
        "nome": input("Digite o nome: "),
        "agencia": input("Digite a agencia: "),
        "conta": input("Digite a conta: "),
        "senha": input("Digite a senha: "),
    }
    lista.append(cliente) #adiciona no final da lista

    print("O cliente {} foi cadastrado com sucesso!\n".format(cliente['nome']))
    print("CPF: {}\n".format(cliente['cpf']))
    print("Agencia: {}\n".format(cliente['agencia']))
    print("Conta: {}\n".format(cliente['conta']))
    print("Senha: {}\n".format(cliente['senha']))
    time.sleep(2)
    os.system("cls")

def principal():
    lista = carregar_cliente() # inicializa a lista de clientes
    while True:
        time.sleep(2)
        os.system("cls")
        adicionar(lista)
        salvar_cliente(lista)
principal()


             
