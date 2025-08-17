def fibonacci(n):
    a, b = 1, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter the number of terms: "))

result = fibonacci(n)
print("Fibonacci series up to", n, "terms:")
for num in result:
    print(num, end=" ")
