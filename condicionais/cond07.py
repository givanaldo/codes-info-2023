print('''
*******************************
CÁLCULO DE GRANDEZAS ELÉTRICAS
*******************************
1. Tensão (em Volt)
2. Resistência (em Ohm)
3. Corrente (em Ampére)
*******************************
Qual grandeza deseja calcular?
''')
opcao = int(input("Opção: "))
if opcao == 1: # U = R.i
    R = int(input("Valor da resistência: "))
    i = int(input("Valor da corrente: "))
    U = R * i
    print(f"Valor da tensão: {U} V")
elif opcao == 2: # R = U / i
    U = int(input("Valor da tensão: "))
    i = int(input("Valor da corrente: "))
    R = U / i
    print(f"Valor da resistência: {R:.0f} \u03A9")
elif opcao == 3: # i = U / R
    U = int(input("Valor da tensão: "))
    R = int(input("Valor da resistência: "))
    i = U / R
    print(f"Valor da corrente: {i:.0f} A")
else:
    print("Opção inválida. Você sabe ler?")

# implementar com repetição