inputed = int(input())

for i in range(inputed):
    if (i % 5) == 0 and (i & 3) == 0:
        print("fizz")
    elif (i % 5) == 0:
        print("buzz")
    elif (i % 3) == 0:
        print("fizzbuzz")
    else:
        print(i)