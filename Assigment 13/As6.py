dict = {"a": 2, "b": 3, "c": 4}

print("Dictionary:", dict)

result = 1
for value in dict.values():
    result *= value

print("Product of all items:", result)