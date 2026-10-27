def mostraIdade(i):
    print("A idade eh ",i)
print("====MENU====")
print("1 - Cadastrar")
print("2 - Consultar")
print("3 - Alterar")
print("4 - Excluir")
print("0 - Sair")

opcao = int(input("Informe a opção: "))

match opcao:
    case 1:
        print("Opção escolhida - CADASTRAR")
        idade = int(input("Informe a idade: "))
        mostraIdade(idade)
    case 2:
        print("Opção escolhida - CONSULTAR")
    case 3:
        print("Opção escolhida - ALTERAR")
    case 4:
        print("Opção escolhida - EXCLUIR")
    case 0:
        print("Opção escolhida - SAIR")
    case _:
        print("Opção inválida!")