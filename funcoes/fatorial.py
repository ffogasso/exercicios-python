def calculoFatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculoFatorial(n-1)
v = int(input("Fatorial de qual numero? "))
fat = calculoFatorial(v)
print(fat)