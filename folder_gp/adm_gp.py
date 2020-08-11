import time
import os

rS = 0
vss = 0
rSu = 0
vssu = 0


while True:
    time.sleep(1)

    print("Banco Digital - Administrativo")
    print("1 - Sangria")
    print("2 - Suprimento")
    print("3 - Relatórios de Produção")
    print("4 - Voltar ao menu principal")
    print("5 - Finalizar Acesso")

    opcaoSelecionada = input("Digite o opção desejada: \n")
      
    if opcaoSelecionada == '1':
        rSO = rS + 1
        print("Registro: ",rSO,'\n')
        input("Registre a finalidade da sangria: "),
        print("\nForma de Pagamento (Mais opções futuramente)")
        print("1 - Dinheiro")
        print("2 - Crédito")
        print("3 - Débito")
        formaPaga = int(input("Digite o opção desejada: "))
        if formaPaga == 1:
            valorSangria = int(input("Digite o valor da sangria: "))
            valorTerciario = vss + valorSangria
        elif formaPaga == 2:
            valorSangria = int(input("Digite o valor da sangria: "))
            valorTerciario = vss + valorSangria
        elif formaPaga == 3:
            valorSangria = int(input("Digite o valor da sangria: "))
            valorTerciario = vss + valorSangria
        conf = input("Realizar sangria(s/n): ")
        if conf == 'n':
            print("Sangria cancelada!\n")
        elif conf == 's':
            print('Sangria feita!\n')
            rS = rSO
            vss = valorTerciario
        else:
            print("\nComando não identificado")

    elif opcaoSelecionada == '2':
        rSup = rSu + 1
        print("Registro do Suprimento: ",rSup)
        valorSuprimento = int(input("Digite o valor da adição: "))
        valorTerciarioo = vssu + valorSuprimento
        input("Digite a finalidade da adição: ")
        confi = input("Salvar suprimento? (s/n)")
        if confi == 'n':
            print("Suprimento cancelado!\n")
        elif confi == 's':
            print('Suprimento realizado!\n')
            rSu = rSup
            vssu = valorTerciarioo
        else:
            print("\nComando não identificado")
                 
    elif opcaoSelecionada == '3':
        rSan = str(rS)
        vSan = str(vss)
        rSup = str(rSu)
        vSup = str(vssu)
        print("Relatórios de produção")
        print("Escolha o módulo:")
        print("1 - Relatório da movimentação do dia")
        print("2 - Relatório da movimentação do mês")
        print("3 - Relatório da movimentação do admnistrativo")
        opcao = int(input('Digite a opção: '))
        if opcao == 1:
            arquivo = open('RelatórioDiario.txt', 'w')
            arquivo.write('Este presente relatório busca fornecer as informações de movimentação deste caixa eletrônico\n')
            arquivo.write('A movimentação da sangria de hoje se constituiu em: ')
            arquivo.write(rSan)
            arquivo.write('\nO valor da movimentação da sangria de hoje foi: ')
            arquivo.write(vSan)
            arquivo.write('\nA movimentação do suprimento de hoje se constituiu em: ')
            arquivo.write(rSup)
            arquivo.write('\nO valor da movimentação do suprimento foi: ')
            arquivo.write(vSup)
            arquivo.close()
            
            arquivo = open('RelatórioDiario.txt', 'r')
            unica_string = arquivo.read()
            arquivo.close()
            
        if opcao == 2:
            arquivo = open('RelatórioMensal.txt', 'a+')
            arquivo.write('Este presente relatório busca fornecer as informações de movimentação deste caixa eletrônico sobre o mês')
            arquivo.read()
            arquivo.close()
            
        if opcao == 3:
            arquivo = open('RelatórioAdministrativo.txt', 'a+')
            arquivo.write('Este presente relatório busca fornecer as informações de movimentação deste caixa eletrônico sobre a movimentação do administrativo')
            arquivo.read()
            arquivo.close()
            
    elif opcaoSelecionada == '5':
        print("Até mais!")
        break
