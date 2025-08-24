def reverse(num,rev=0):
    if(num == 0):
        return rev
    digit  = num % 10
    rev  = rev * 10 + digit
    return reverse(num//10,rev)
num = int(input("Enter the number :"))
reversed_num = reverse(num)
print(f"Reversed number: {reversed_num}")
