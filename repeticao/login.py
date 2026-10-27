for i in range(1, 4):
    usuario = input("Digite o seu usuario: ")
    senha = input("Digite a sua senha: ")
    acesso = input("Possui acesso especial: (S/N)").upper()
    if usuario == "admin" and senha == "monster123":
        print("Acesso liberado.")
        print("Bem-Vindo(a) ao sistema.")
        break
    elif acesso == "S":
        print("Acesso liberado.")
        print("Bem-Vindo(a) ao sistema.")
        break
    else:
        print("Usuario ou senha invalido(a), tente novamente.")
else:
    print("Acesso bloqueado, numero maximo de tentativas atingido.")