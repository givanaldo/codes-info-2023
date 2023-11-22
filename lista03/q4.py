# Sequência de Fibonnacci
# F(n=8) = 1 1 2 3 5 8 13 21
n = int(input('Valor de n: '))
f = [1, 1]
if n < 1:
    print('Valor inválido')
elif n == 1:
    print(f'F({n}) = 1')
elif n == 2:
    print(f'F({n}) = 1 1')
else:
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    print(f'F({n}) =', end=' ')
    for item in f:
        print(f'{item}', end=' ')