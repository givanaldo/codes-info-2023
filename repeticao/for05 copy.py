texto = '''
um texto qualquer de várias linhas você vai 
procurar por uma palavra no texto e dizer se a 
palavra existe e quantas vezes ela aparece no texto
'''
palavras = texto.split()
palavra = input("Palavra: ")
n = 0
for p in palavras:
    if p == palavra:
        n = n + 1
if n == 0:
    print(f'A palavra {palavra} não foi encontrada')
else:
    print(f'A palavra {palavra} foi encontrada {n} vezes')