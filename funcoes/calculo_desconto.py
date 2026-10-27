def calculoDesconto(preco, desconto):
    return preco - (preco * desconto / 100)
 
 
preco = float(input("Qual o valor do produto: "))
desconto = float(input("Qual a % de desconto? "))
 
if preco >= 0 and 0 <= desconto <= 100:
    valorFinal = calculoDesconto(preco, desconto)
    print(f"Valor final: R$ {valorFinal:.2f}")
else:
    print("Valor invalido, tente novamente!")
