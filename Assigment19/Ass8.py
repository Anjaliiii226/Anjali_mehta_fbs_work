def fibo(num):
    a , b = 0 , 1
    while a<=num:
        yield a
        a , b = b , a + b
num = int(input("Enter the number:"))
for i in fibo(num):
    print(i , end = " ")