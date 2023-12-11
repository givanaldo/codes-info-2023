texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.
'''
lista = texto.split()
pontuacao = ',.:'
for p in pontuacao:
    for i, palavra in enumerate(lista):
        lista[i] = palavra.replace(p, "")
print(lista)

import string
print(string.digits)
print(string.punctuation)
print(string.ascii_letters)
