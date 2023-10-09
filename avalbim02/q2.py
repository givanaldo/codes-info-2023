print('''*****************************
Volume de Formas Geométricas
*****************************
[1] Esfera
[2] Cilindro
[3] Paralelepípedo''')
op = int(input('Opção: '))
pi = 3.14159
if op == 1:
    raio = int(input('Raio: '))
    volume = 4/3 * pi * raio**3
    print(f'Volume da esfera = {volume}')
elif op == 2:
    raio = int(input('Raio: '))
    h = int(input('Altura: '))
    volume = pi * raio**2 * h
    print(f'Volume do cilindro = {volume}')
elif op == 3:
    l = int(input('Largura: '))
    c = int(input('Comprimento: '))
    h = int(input('Altura: '))
    volume = l * c * h
    print(f'Volume do paralelepípedo = {volume}')
else:
    print ('Opção inválida')