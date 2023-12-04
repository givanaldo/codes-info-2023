semana = ["", "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
n = int(input("Número: "))
if 1 <= n <= 7:
    print(semana[n])
else:
    print("dia inválido!")