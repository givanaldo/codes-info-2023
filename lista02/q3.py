peso = float(input('Peso dos peixes: '))
if peso <= 50:
    excesso = 0
    multa = 0
else:
    excesso = peso - 50
    multa = 4 * excesso
print(f"Excesso: {excesso} Kg.")
print(f"Multa: R$ {multa:.2f}.")