while True:
    n, m = input().split()
    n, m = int(n), int(m)
    if n <= 0 or m <= 0:
        break
    if n > m:
        n, m = m, n
    soma = 0
    for i in range(n, m+1):
        print(i,  end=' ')
        soma += i
    print(f'Sum={soma}')
