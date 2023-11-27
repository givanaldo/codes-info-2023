import random
lista = []
for _ in range(10):
    lista.append(random.randint(1, 100))
print(lista)
print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')