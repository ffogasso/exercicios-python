import random

print("Jogo Jokenpo")
opcoes = ["Pedra", "Papel", "Tesoura"]
pc = random.choice(opcoes)
jogador = input("Escolha entre pedra, papel e tesoura:  ").strip().capitalize()
print("PC escolheu", pc)
print("Você escolheu", jogador)

if jogador == pc:
    print("Empate!")
elif jogador == "Pedra":
    if pc == "Tesoura":
        print("Você venceu!")
    else:
        print("Você perdeu!")
elif jogador == "Tesoura":
    if pc == "Papel":
        print("Você venceu!")
    else:
        print("Você perdeu!")
elif jogador == "Papel":
    if pc == "Pedra":
        print("Você venceu!")
    else:
        print("Você perdeu!")
else:
    print("Opção inválida!")
