string = input("Enter a string: ")

vowels = "aeiouAEIOU"   
count = 0

for i in string:
    for v in vowels:       
        if i == v:
            count += 1
            break          

print("Original String:", string)
print("Number of vowels:", count)