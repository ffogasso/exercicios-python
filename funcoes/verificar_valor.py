def verificarValor(v):
    result =""
    if (v >= 0):
        result = "P"
    else:
        result = "N"
    return result
valor = int(input("Informe um valor inteiro: "))
r = verificarValor(valor)
print("O valor é",r)