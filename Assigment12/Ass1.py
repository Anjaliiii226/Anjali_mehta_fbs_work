string = input("Enter a string: ")

result = ""   

for  i in string:
    if i == 'a':         
        result += '$'     
    else:
        result += i     

print("Original String:", string)
print("Modified String:", result)