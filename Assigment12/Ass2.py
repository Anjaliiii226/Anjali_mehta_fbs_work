string = input("Enter a string: ")
n = int(input("Enter the index of character to remove: "))

if n < 0 or n >= len(string):
    print("Invalid index!")
else:
    result = ""  
    for i in range(len(string)):
        if i != n:        
            result += string[i]
    print("Original String:", string)
    print("Modified String:", result)