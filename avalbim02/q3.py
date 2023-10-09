n1 = float(input('Item 1: '))
n2 = float(input('Item 2: '))
n3 = float(input('Item 3: '))
n4 = float(input('Item 4: '))
n5 = float(input('Item 5: '))
total = n1 + n2 + n3 + n4 + n5
print(f'Total: R$ {total:.2f}')
if total > 200:
    print('Obrigado pela preferência!')
else:
    print('Poderia ter gastado mais!')