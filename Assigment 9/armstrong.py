def countDigit(num):
    if num == 0:
        return 0
    return 1 + countDigit(num // 10)


def calculateSum(num, count):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** count) + calculateSum(num // 10, count)


def checkArmstrong(num):
    count = countDigit(num)
    total = calculateSum(num, count)
    return total == num

num = int(input("Enter the number: "))
if checkArmstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")