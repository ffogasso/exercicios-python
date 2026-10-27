salario = float(input("Digite o seu salário: "))
tempo_de_servico = int(input("Digite o seu tempo de serviço (em anos): "))

# reajuste conforme a faixa salarial
if salario <= 500:
    reajuste = 0.25
    print("Você tem um reajuste de 25%!")
elif salario <= 1000:
    reajuste = 0.20
    print("Você tem um reajuste de 20%!")
elif salario <= 1500:
    reajuste = 0.15
    print("Você tem um reajuste de 15%!")
elif salario <= 2000:
    reajuste = 0.10
    print("Você tem um reajuste de 10%!")
else:
    reajuste = 0
    print("Você não possui reajuste!")

# bônus conforme o tempo de serviço
if tempo_de_servico <= 1:
    bonus = 0
    print("Você não possui bônus!")
elif tempo_de_servico <= 3:
    bonus = 100
    print("Você possui um bônus de R$100,00!")
elif tempo_de_servico <= 6:
    bonus = 200
    print("Você possui um bônus de R$200,00!")
elif tempo_de_servico <= 10:
    bonus = 300
    print("Você possui um bônus de R$300,00!")
else:
    bonus = 500
    print("Você possui um bônus de R$500,00!")

aumento = salario * reajuste
salario_atual = salario + aumento + bonus
print(f"Salário atual: R$ {salario_atual:.2f}")
