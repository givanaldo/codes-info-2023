valor = float(input("Valor: "))
desconto = int(input("Desconto:"))
v_desconto = valor * (desconto/100)
final = valor - v_desconto
print(f"Valor: R$ {valor:.2f}")
print(f"Desconto: R$ {v_desconto:.2f}")
print(f"Valor final: R$ {final:.2f}")