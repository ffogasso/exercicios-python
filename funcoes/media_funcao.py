def calculaMedia(a, b, c, d):
    media = (a + b + c + d) / 4
    return media


def situacaoAluno(m):
    if m >= 7:
        print("Aprovado")
    elif 3 <= m < 7:
        print("Exame")
    else:
        print("Reprovado")


n1 = float(input("Informe a nota 1: "))
n2 = float(input("Informe a nota 2: "))
n3 = float(input("Informe a nota 3: "))
n4 = float(input("Informe a nota 4: "))

media = calculaMedia(n1, n2, n3, n4)
print(f"Média: {media:.2f}")
situacaoAluno(media)
