def sum_of_odd(n):
    total = 0
    for i in range(1, n + 1, 2):   
        total += i
    return total

n = int(input("Enter the value of n: "))

result = sum_of_odd(n)
print("The sum of all odd numbers between 1 and", n, "is:", result)
sum_of_odd