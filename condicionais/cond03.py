temperatura = int(input('Temperatura: '))

if temperatura < 0:
    print('Congelando.')
elif temperatura <= 20:
    print('Frio.')
elif temperatura <= 25:
    print('Agradável.')
elif temperatura <= 35:
    print('Quente.')
else:
    print('Escaldante!')

    