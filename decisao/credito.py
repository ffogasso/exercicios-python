renda = int(input("Digite a sua renda:  "))
resposta = input("Seu nome está limpo?  (s/n)  ").strip().lower()
nome_limpo = resposta in ("s", "sim")

if renda >= 3500 and nome_limpo:
    print("Crédito Aprovado!")
elif renda >= 2500 and nome_limpo:
    print("Crédito Aprovado parcialmente!")
else:
    print("Crédito Reprovado!")
