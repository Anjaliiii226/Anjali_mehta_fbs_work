string = input("Enter a string: ")

result = ""

for i in range(len(string)):
    if i % 2 == 0:         
        result += string[i]

print("Original String:", string)
print("Modified String (odd index chars removed):", result)