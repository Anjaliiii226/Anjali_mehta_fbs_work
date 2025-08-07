num = int(input("Enter a three-digit number: "))

if 100 <= num <= 999:
    
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    total = hundreds + tens + ones

    print("Sum of the digits:", total)

else:
    
    print("Please enter a valid three-digit number.")