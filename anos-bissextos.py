import funcoes as f
inicio = int(input("Início: "))
fim = int(input("Fim: "))
for ano in range(inicio, fim+1):
    if f.bissexto(ano) == True:
        print(f'{ano} é bissexto')
    else:
        print(f'{ano} não é bissexto')