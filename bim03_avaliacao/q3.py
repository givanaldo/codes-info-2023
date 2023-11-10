sucesso = [0, 0, 0]
total = [0, 0, 0]
n = int(input())
for i in range(n):
    jogador = input()
    a, b, c = input().split()
    x, y, z = input().split()
    total[0] += int(a)
    total[1] += int(b)
    total[2] += int(c)
    sucesso[0] += int(x)
    sucesso[1] += int(y)
    sucesso[2] += int(z)
saque = (sucesso[0] / total[0])*100
bloqueio = (sucesso[1] / total[1])*100
ataque = (sucesso[2] / total[2])*100
print(f'Pontos de Saque: {saque:.2f} %.')
print(f'Pontos de Bloqueio: {bloqueio:.2f} %.')
print(f'Pontos de Ataque: {ataque:.2f} %.')
