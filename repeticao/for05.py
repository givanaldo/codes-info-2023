texto = '''
um texto qualquer de várias linhas
você vai procurar por uma palavra no 
texto e dizer se a palavra existe e 
quantas vezes ela aparece no texto
'''
palavras = texto.split()
palavra = input("Palavra: ")
ocorrencias = 0
for p in palavras:
    if palavra == p:
        ocorrencias += 1
if ocorrencias == 0:
    print(f"Palavra '{palavra}' não encontrada.")
else:    
    print(f"Palavra '{palavra}' encontrada {ocorrencias} vezes.")