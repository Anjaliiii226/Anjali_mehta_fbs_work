def sum_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter the value of n: "))

result = sum_series(n)
print("The sum of series 1 + 2 + ... +", n, "is:", result)

sum_series()