dict = {"name": "Anjali", "age": 21, "city": "Delhi", "country": "India"}

print("Original Dict:", dict)

n = input("Enter the key to remove: ")

if n in dict:
    del dict[n]
    print(f"Updated Dict after removing '{n}':", dict)
else:
    print(f"Key '{n}' not found in the dict.")
