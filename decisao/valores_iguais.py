valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 == valor2 == valor3:
    print("Os valores são todos iguais.")
elif valor1 > valor2 and valor1 > valor3:
    print("Valor 1 é maior que valor 2 e valor 3.")
elif valor2 > valor1 and valor2 > valor3:
    print("Valor 2 é maior que valor 1 e valor 3.")
elif valor3 > valor1 and valor3 > valor2:
    print("Valor 3 é maior que valor 1 e valor 2.")
else:
    print("Existem dois valores empatados no topo como os maiores.")