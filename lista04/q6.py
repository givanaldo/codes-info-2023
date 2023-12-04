palavra = input("Palavra: ")
# palavra.replace("á", "a")
invertida = palavra[::-1]
print(f"Palavra invertida: {invertida}")
if palavra.upper() == invertida.upper():
    print(f"{palavra} é palíndroma")
else:
    print(f"{palavra} não é palíndroma")