usuario = senha = "aaaa"
while usuario == senha:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == senha:
        print("ERRO!")
    else:
        print("OK!")