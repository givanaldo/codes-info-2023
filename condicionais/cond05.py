print('== Operadora Tchau ==')
min = int(input('Minutos utilizados: '))
if min < 200:
    preço = 0.20
else:
    if min <= 400:
        preço = 0.18
    else:
        preço = 0.15
conta = min * preço
print(f'Conta telefônica: R$ {conta:.2f}')

