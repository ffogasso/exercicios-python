def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)
print(f"O IMC É: {imc:.2f}")