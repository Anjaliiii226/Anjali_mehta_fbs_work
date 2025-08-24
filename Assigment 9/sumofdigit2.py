def sumofdigit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumofdigit(n // 10)
    
num = int(input("Enter the number :"))
if num < 0:
    num = -num
result  = sumofdigit(num)
print(f"Sum of digit of number is:{result}")