import random as rd
lista = []
for _ in range(10):
    lista.append(rd.randint(1, 100))
print(lista)
lista.sort()
print(f'Maior: {lista[len(lista)-1]}')
print(f'Menor: {lista[0]}')