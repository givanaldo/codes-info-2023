nota = -1
while nota < 0 or nota > 10:
    nota = int(input("Nota (0-10):"))
    if nota < 0 or nota > 10:
        print(f"Nota {nota} inválida!")
    else:
        print(f"Nota {nota} válida! #SEXTOU")