num = int(input("Enter a three-digit number: "))


if 100 <= num <= 999:
    
    reverse = int(str(num)[::-1])
    print("Reversed number:", reverse)
else:
    print("Please enter a valid three-digit number.")