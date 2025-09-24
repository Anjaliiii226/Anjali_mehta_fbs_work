string = input("Enter a string: ")
char_count = 0
for ch in string:
    char_count += 1
word_count = 0
in_word = False   

for ch in string:
    if ch != " " and not in_word:
        word_count += 1   
        in_word = True
    elif ch == " ":
        in_word = False   

print("Original String:", string)
print("Number of characters:", char_count)
print("Number of words:", word_count)