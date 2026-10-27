import random

vitorias_jogador = 0
vitorias_pc = 0
empates = 0

while True:
    jogador = random.randint(1, 6)
    pc = random.randint(1, 6)
    print(f"Você tirou: {jogador}.")
    print(f"Computador tirou: {pc}.")
    if pc > jogador:
        print("O computador venceu.")
        vitorias_pc += 1
    elif jogador > pc:
        print("Você venceu.")
        vitorias_jogador += 1
    else:
        print("Empate!")
        empates += 1

    jogar = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
    if jogar not in ("S", "SIM"):
        print("Jogo encerrado")
        break

print(f"\nPlacar final -> Você: {vitorias_jogador} | Computador: {vitorias_pc} | Empates: {empates}")
