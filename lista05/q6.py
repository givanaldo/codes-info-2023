numero = int(input("Decimal: "))
decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romano = ['M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
resultado = ""
for i in range(len(decimal)):
    count = int(numero / decimal[i])
    resultado += romano[i] * count
    numero = int(numero % decimal[i])
print(f"Romano: {resultado}")