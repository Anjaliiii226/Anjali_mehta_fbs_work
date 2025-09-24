n = input("Enter a string: ")

words = n.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequency Dict:", freq)