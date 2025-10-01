sentences = [
    "python is easy to learn",
]
words = []
for sentence in sentences:
    words.extend(sentence.split())

unique_words = set(words)

word_freq = {}
for word in unique_words:
    word_freq[word] = words.count(word)

print("Unique words:", unique_words)
print("Word frequencies:")
for word, freq in word_freq.items():
    print(word, ":", freq)
