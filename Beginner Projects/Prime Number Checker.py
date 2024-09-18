x = int(input('Pls enter a number: '))
for y in range(2, x):
    if(x % y) == 0:
        print(x, 'is not prime')
        break
    else:
        print(x, 'is prime')
        break