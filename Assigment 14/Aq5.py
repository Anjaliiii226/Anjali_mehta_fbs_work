def prefix(words):
    if not words:
        return ""
    
    shortest = min(words, key=len)
    
    prefix = ""
    for i in range(len(shortest)):
        # Take all characters at index i from each word
        chars = set(word[i] for word in words)
        
        if len(chars) == 1:
            prefix += chars.pop()
        else:
            break
    return prefix

words = ["flower", "flow", "flight"]
print("Longest Common Prefix:", prefix(words))