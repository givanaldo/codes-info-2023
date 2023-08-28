n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))
# MAIOR
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3
# MENOR
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3
print(f"Maior: {maior}")
print(f"Menor: {menor}")
