user = input("Digite seu usuario:   ")
senha = input("Digite sua senha:   ")

if user == "admin" and senha == "123":
    print("Acesso total!")
elif user == "professor" and senha == "123":
    print("Acesso intermediário")
elif user == "aluno" and senha == "123":
    print("Acesso básico")
else:
    print("Usuario/Senha Incorreto(a)")