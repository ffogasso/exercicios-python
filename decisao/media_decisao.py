nota1 = float(input("Digite a nota um:  "))
nota2 = float(input("Digite a nota dois:  "))
nota3 = float(input("Digite a nota três:  "))
nota4 = float(input("Digite a nota quatro:  "))

if nota1 < 0 or nota1 > 10:
    print("nota um inválida")
elif nota2 < 0 or nota2 > 10:
    print("nota dois inválida")
elif nota3 < 0 or nota3 > 10:
    print("nota três inválida")
elif nota4 < 0 or nota4 > 10:
    print("nota quatro inválida")
else:
    soma = nota1 + nota2 + nota3 + nota4
    media = soma / 4
    print(f"Média: {media:.2f}")
    if media >= 7:
        print("aluno aprovado")
    else:
        print("aluno reprovado")
