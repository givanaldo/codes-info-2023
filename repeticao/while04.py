tabuada = 1
while tabuada <= 10:
    n = 1
    print(f'Tabuada de {tabuada}')
    print('-------------')
    while n <= 10:
        resultado = tabuada * n
        print(f'{tabuada} x {n} = {resultado}')
        n = n + 1
    print('-------------')
    tabuada = tabuada + 1
