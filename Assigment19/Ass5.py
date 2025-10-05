num = input("Enter the letter:")
words = [i for i in num.split() if len(i) < 5]
print("Words with less than 5 letters:",words)
