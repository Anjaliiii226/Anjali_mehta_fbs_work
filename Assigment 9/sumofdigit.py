def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num -1)
    
def sumofdigit(n):
    if n==0:
        return 0
    else:
        return factorial(n)  + sumofdigit(n-1)
n = int(input("Enter the value of n: "))

result  = sumofdigit(n)
print(f"Sum of series 1! + 2! + 3! + ... + {n}! = {result}")
