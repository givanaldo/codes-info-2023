n = int(input())
for i in range(n):
  valor = int(input())
  if valor == 0:
    print("NULL")
  else:
    if valor % 2 == 0:
      print("EVEN", end=" ")
    else:
      print("ODD", end=" ")
    if valor < 0:
      print("NEGATIVE")
    else:
      print("POSITIVE")
