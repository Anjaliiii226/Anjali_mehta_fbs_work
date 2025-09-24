n = int(input("Enter the value of n: "))

dict = {}
for x in range(1, n + 1):
    dict[x] = x * x

# print result
print("Generated Dictionary:", dict)