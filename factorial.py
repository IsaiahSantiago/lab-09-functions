def factorial(n):
    factor = 1
    for i in range(1, n + 1, 1):
        factor = factor * i
    return factor


userInput = input("Number to calculate the factorial please:")
usernum = int(userInput)
print(factorial(usernum))

