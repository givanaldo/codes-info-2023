# Para formar um triângulo, a soma de dois lados
# tem que ser maior que o terceiro lado

a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))

if a+b>c and a+c>b and b+c>a:
    # Equilátero, Isóceles ou Escaleno
    if a == b == c:
        print('Triângulo Equilátero.')
    elif a == b or a == c or b == c:
        print('Triângulo Isóceles.')
    else:
        print('Triângulo Escaleno.')
else:
    print('Os lados não formam um triângulo!')