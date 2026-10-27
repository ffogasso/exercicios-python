def calculaMedia(a, b, c, d):
    media = (a + b + c + d) / 4
    return media


def calculaMediaPonderada(a, b, c, d, p1, p2, p3, p4):
    soma_pesos = p1 + p2 + p3 + p4
    media = (a * p1 + b * p2 + c * p3 + d * p4) / soma_pesos
    return media


def situacaoAluno(m):
    if m >= 7.0:
        print(f"Aprovado (Média: {m:.2f})")
    elif 3.0 <= m < 7.0:
        print(f"Exame (Média: {m:.2f})")
    else:
        print(f"Reprovado (Média: {m:.2f})")


nota1 = float(input("Digite a 1ª nota: "))
peso1 = float(input("Digite o peso da 1ª nota: "))

nota2 = float(input("Digite a 2ª nota: "))
peso2 = float(input("Digite o peso da 2ª nota: "))

nota3 = float(input("Digite a 3ª nota: "))
peso3 = float(input("Digite o peso da 3ª nota: "))

nota4 = float(input("Digite a 4ª nota: "))
peso4 = float(input("Digite o peso da 4ª nota: "))

media_final = calculaMediaPonderada(
    nota1, nota2, nota3, nota4, peso1, peso2, peso3, peso4
)

situacaoAluno(media_final)