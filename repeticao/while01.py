# exiba os X primeiros múltiplos de um número 
# que o usuário digitar.
num = int(input('Número: '))
n_multiplos = int(input('Quantidade de múltiplos:'))
i = 1
while i <= n_multiplos:
    print(num * i)
    i = i + 1