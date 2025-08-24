def reversenumber(num, rev=0):
    if num == 0:
        return rev
    rev = rev * 10 + (num % 10)
    return reversenumber(num // 10, rev)

num = int(input("Enter a number: "))
result = reversenumber(num)
print(f"The reverse of {num} is {result}")