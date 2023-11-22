total = 0
for i in range(5):
    item = float(input("Valor: "))
    total = total + item
print(f"Total = R$ {total:.2f}")
print("Obrigado pela preferência!" if total > 200 else "Poderia ter gastado mais!.")