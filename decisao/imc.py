peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / altura ** 2
print(f"Seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc < 25:
    print("Você está com peso saudável")
elif imc < 30:
    print("Você está com excesso de peso")
elif imc < 35:
    print("Você está com obesidade de grau 1")
elif imc < 40:
    print("Você está com obesidade de grau 2")
else:
    print("Você está com obesidade de grau 3")
