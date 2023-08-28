# 1 litro -> 3 metros quadrados
# lata -> 18 litros (R$ 80,00) -> 54 m2
area = int(input("Área a ser pintada: "))
latas = area // 54
if (area % 54 != 0):
    latas += 1
print(f"Latas: {latas}")

