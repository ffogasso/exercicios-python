valor = float(input("Valor do deposito mensal (R$): "))
meses = int(input("Quantidade de meses: "))
saldo = 0
for mes in range (1, meses + 1):
    saldo += valor
    print(f"Mes {mes}: saldo acumulado = R$ {saldo:.2f}")