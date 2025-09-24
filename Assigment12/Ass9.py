str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
def get_length(s):
    count = 0
    for ch in s:
        count += 1
    return count
len1 = get_length(str1)
len2 = get_length(str2)
print("First String:", str1)
print("Second String:", str2)
if len1 > len2:
    print("Larger String is:", str1)
elif len2 > len1:
    print("Larger String is:", str2)
else:
    print("Both strings are equal in length")