string = input("Enter a string: ")
count = 0
for ch in string:
    if ch.islower():   
        count += 1
print("Original String:", string)
print("Number of lowercase characters:", count)