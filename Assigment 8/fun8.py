def digit(num):
    total = 0
    while num > 0:
        digit = num % 10   
        total += digit
        num //= 10         
    return total

number = int(input("Enter a number: "))

result = digit(number)
print("The sum of digits of", number, "is:", result)
digit()
