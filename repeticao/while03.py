num = int(input("Número: "))
fatorial = 1
i = num
while i > 1:
    fatorial = fatorial * i
    i = i - 1
print(f'F({num}) = {fatorial}')