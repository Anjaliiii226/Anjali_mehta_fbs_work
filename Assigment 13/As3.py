dict = {"name": "Anjali", "age": 21, "city": "Delhi"}

key = input("Enter the key to check: ")

if key in dict:
    print(f"Yes, the key '{key}' exists with value: {dict[key]}")
else:
    print(f"No, the key '{key}' does not exist in the dictionary.")