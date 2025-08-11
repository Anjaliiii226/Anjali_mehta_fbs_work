num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the number to check divisibility: "))

print(f"Numbers between {num1} and {num2} divisible by {num3} are:")
for i in range(num1, num2 + 1):
    if i % num3 == 0:
        print(i, end=" ")