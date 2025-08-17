def reverse(num):
    rev = 0
    while num > 0:
        digit = num % 10      
        rev = rev * 10 + digit 
        num //= 10             
    return rev

# Main program
number = int(input("Enter a number: "))

result = reverse(number)
print("The reverse of", number, "is:", result)
reverse()