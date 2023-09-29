texto = input("Texto: ")
vogais = "AÁÃÂEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=" ")