def power(m,n):
    if n == 0:
        return 1 
    else:
        return n*power(m,n-1)
    
m = int(input(f'Enter the base :'))
n = int(input(f'Enter the exponential:'))
result = power(m,n)
print(f"{m} is the raise the power{n} is {result}")