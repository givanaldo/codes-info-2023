saldo = 2000.00
saque = float(input("Valor do saque: "))
status = "Sucesso" if saque <= saldo else "Falha"
print(f"{status} no saque.")