import re
from collections import Counter

def count_word_frequency(text):

    words = re.findall(r"\b\w+\b", text.lower())


    return Counter(words)
