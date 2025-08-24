def fibanacci(n):
    if n== 0 :
        return 0
    elif n == 1:
        return 1 
    else:
        return fibanacci(n-1) + fibanacci(n -2)
def fibanacciseries(n):

    for i in range(n):

        print(fibanacci(i),end=' ')

num = int(input("Enter the number :"))
if num<=0:
    print('Enter the  positive number')
    
else:
    print(f'Fibanacci series up to {num} , num')
    fibanacciseries(num)

