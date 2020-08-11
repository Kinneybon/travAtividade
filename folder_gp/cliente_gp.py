import os
import time


def carregar_cliente():
    lista = []

    try:
        arquivo = open("cliente.txt", "r")

        for linha in arquivo.readlines():
            coluna = linha.strip().split("#")
            cliente = {
                "nome": coluna[1],
                "razao": coluna[0],
                "cnpj": coluna[2],
                "ie": coluna[3],
            }
            lista.append(cliente)

        arquivo.close()
    except FileNotFoundError:
        print("Arquivo não existe - Criar....")
        pass

    return lista


def salvar_cliente(lista):
    arquivo = open("cliente.txt", "w")

    for cliente in lista:
        arquivo.write('{}#{}#{}#{}1\n'.format(cliente['razao'], cliente['nome'], cliente['cnpj'], cliente['ie']))

    arquivo.close()
    print(".")
    print(".")
    print(".")
    from folder_gp_1.Main import Proj
    main = Proj()
    main.init()


def existe_cliente(lista, nome):
    if len(lista) > 0:
        for cliente in lista:
            if cliente['nome'] == nome:
                return True
    return False


def adicionar(lista):
    while True:
        nome = input("Digite o nome do banco que será cadastrado: ")

        if not existe_cliente(lista, nome):
            break
        else:
            print("Esse nome já foi utilizado.")
            print("Por favor, digite um novo nome.")
            time.sleep(2)
            os.system("cls")

    cliente = {
        "nome": nome,
        "razao": input("Digite a razão social: "),
        "cnpj": input("Digite o cpnj: "),
        "ie": input("Digite a inscrição estadual: "),
    }
    lista.append(cliente)

    print("O cliente {} foi cadastrado com sucesso!\n".format(cliente['nome']))
    print("Razão social: {}\n".format(cliente['razao']))
    print("CNPJ: {}\n".format(cliente['cnpj']))
    print("Inscrição estadual: {}\n".format(cliente['ie']))
    time.sleep(2)
    os.system("cls")


def alterar():
    pass


def excluir():
    pass


def buscar():
    pass


def listar(lista):
    print("Bancos cadastrados: ")
    if len(lista) > 0:
        for i, cliente in enumerate(lista):
            print("Contato {}".format(i + 1))
            print("\tRazao: {}".format(cliente['razao']))
            print("\tNome: {}".format(cliente['nome']))
            print("\tCnpj: {}".format(cliente['cnpj']))
            print("\tIe: {}".format(cliente['ie']))
            print("===============================================")
        print("Quantidade de Clientes: {}\n".format(len(lista)))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def principal():
    lista = carregar_cliente()
    while True:
            adicionar(lista)
            salvar_cliente(lista)
            
            
principal()
