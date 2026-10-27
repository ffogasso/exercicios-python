dias = int(input("Quantos dias o carro ficou alugado?   "))
km = float(input("Quantos Km foram rodados?	"))
valor_km = 0.15
valor_dia = 60.00

total_diaria = dias * valor_dia
total_km = km * valor_km
total_a_pagar = total_diaria + total_km

print(f"\nValor Total a pagar: R$ {total_a_pagar:.2f}")
print(f"Valor Total das diárias: R$ {total_diaria:.2f}")
print(f"Valor Total dos km: R$ {total_km:.2f}")