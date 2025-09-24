string = input("Enter a string: ")
letters = 0
digits = 0
for ch in string: 
    if '0' <= ch <= '9':
        digits += 1
    elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        letters += 1
print("Original String:", string)
print("Number of letters:", letters)
print("Number of digits:", digits)