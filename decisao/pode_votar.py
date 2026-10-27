ano = int(input("Digite o ano em que você nasceu: "))
ano_atual = int(input("Em que ano estamos: "))
idade = ano_atual - ano
print("Idade:", idade)

# o voto é permitido a partir dos 16 anos
if idade >= 16:
    print("Você pode votar")
else:
    print("Você não pode votar")
