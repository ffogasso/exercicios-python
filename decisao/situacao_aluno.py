nota1 = float(input("Digite a primeira nota:   "))
nota2 = float(input("Digite a segunda nota:    "))
frequencia = int(input("Digite a sua frequencia:   "))
media = (nota1 + nota2) /2

if media >= 7 and frequencia >= 75:
    print("Aprovado!")
elif media >= 6 and frequencia >= 75:
    print("Exame!")
else:
    print("Reprovado!")