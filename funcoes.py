def dataporextenso(data):
    d, m, a = map(int, data.split("/"))
    meses = ['', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return f"{d} de {meses[m]} de {a}."

def raizquadrada(n):
    from math import sqrt
    return sqrt(n)

def bissexto(ano):
    if (ano%400==0) or (ano%4==0 and ano%100!=0):
        return True
    else:
        return False

def eq2grau(a, b, c):
    import math
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