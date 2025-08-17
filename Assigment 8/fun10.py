def palindrome(num):
    original = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return original == rev

number = int(input("Enter a number: "))

if palindrome(number):
    print(number, "is a Palindrome number.")
else:
    print(number, "is NOT a Palindrome number.")