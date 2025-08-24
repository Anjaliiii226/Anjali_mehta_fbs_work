def sumofn(num):
    if(num==0): 
        return 0
    else:
        return num + sumofn(num-1)
    
num = int(input("Enter the number :"))
result = sumofn(num)
print(f"sum of digit of n :{result}")