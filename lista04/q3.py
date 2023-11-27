data = input("Data: ")
dia, mes, ano = map(int, data.split("/"))
# 12/05/2020 => [12, 05, 2020]
if dia not in range(1, 32):
    print("Data inválida")
elif mes not in range(1, 13):
    print("Data inválida")
elif ano < 0:
    print("Data inválida")
else:
    print("Data OK")