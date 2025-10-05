num = input("Enter a sentence: ")
length = {word: len(word) for word in num.split()}
print("Length of each word:", length)
