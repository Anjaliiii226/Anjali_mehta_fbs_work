def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_of_factorial_series(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

n = int(input("Enter the value of n: "))

result = sum_of_factorial_series(n)
print("The sum of series 1! + 2! + ... +", n, "! is:", result)

