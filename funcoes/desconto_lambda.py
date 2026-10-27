preco = float(input("Preço do produto: R$ "))
desconto = float(input("Percentual de desconto (%): "))

valor_final = lambda p, d: p - (p * d / 100)

print(f"Valor final: R$ {valor_final(preco, desconto):.2f}")
