def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * factorial(n -1)
num = int(input("Enter the number :"))
if num < 0 :
    print(f"factorial  is not defined for the negative number:")
else: 
    result= factorial(num)
    print(f"factorial of sum :{result}")