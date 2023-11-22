popA = 80000  # crescimento de 3%
popB = 200000 # crescimento de 1.5%

# Em quantos anos a população A
# ultrapassa ou iguala a população B???
n = 0
while popA <= popB:
    popA = popA + 0.03*popA
    popB = popB + 0.015*popB
    n += 1
print(f"Demorou {n} anos.")
print(f"A = {popA:.0f}")
print(f"B = {popB:.0f}")