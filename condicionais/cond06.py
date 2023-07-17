n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))
n4 = int(input('N4: '))
media = (n1*2+n2*2+n3*3+n4*3)/10
print(f'Média = {media:.0f}')
if media >= 60:
    print('Situação: Aprovado')
elif media >= 30:
    print('Situação: Recuperação')
else:
    print('Situação: Reprovado')