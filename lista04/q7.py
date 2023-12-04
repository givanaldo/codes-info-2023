#Entre com uma sequência numérica (Ex: 4329954039)
#e informe se você quer visualizar a sequência ao
#contrário, de dois em dois ou de três em três.
while(True) :
    seq = input("Sequência: ")
    print("1 - Ao contrário")
    print("2 - Dois em dois")
    print("3 - Três em três")
    print("0 - SAIR")
    op = int(input("Opção: "))
    if op == 1:
        print(f"=> {seq[::-1]}")
    elif op == 2:
        print(f"=> {seq[::2]}")
    elif op == 3:
        print(f"=> {seq[::3]}")
    elif op == 0:
        break
    else:
        print("Você sabe ler?!?!?!")