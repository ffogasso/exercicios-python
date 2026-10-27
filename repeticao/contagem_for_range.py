import time

# contagem regressiva
for num in range(10, 0, -1):
    time.sleep(1)  # espera 1 segundo
    print(num)
print("COMEÇOU!!!")

# soma de números
numeros = [1, 5, 8]
soma = 0
for numero in numeros:
    soma += numero
print("A soma é:", soma)
