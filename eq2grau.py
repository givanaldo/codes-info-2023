import math
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))
delta = b*b - 4*a*c
if delta < 0:
    print("não existem raízes reais.")
elif delta == 0:
    x = -b / (2*a)
    print(f"x1 = x2 = {x}")
else: 
    x1 = (-b + math.sqrt(delta) ) / (2*a)
    x2 = (-b - delta**0.5 ) / (2*a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")