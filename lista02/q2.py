# Um ano é bissexto caso ele seja divisível por 4,
# mas não por 100, ou seja divisível por 400.
ano = int(input("Digite o ano: "))
if (ano%400==0) or (ano%4==0 and ano%100!=0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')