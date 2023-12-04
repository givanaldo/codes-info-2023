x = 1 
while x < 101:
    if x%3==0 and x%5==0:
        print("fizzbuzz")
    elif x%3==0:
        print("fizz")
    elif x%5==0:
        print("buzz")
    else:
        print(f"{x}")
    x = x+1
    
