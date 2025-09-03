li = [10,20,30,40,50,60]
m = int(input("Enter the number in m: "))
n = int(input("Enter the number in n :"))

result = []

for i in li :
 
 if(i%m==0 and i%n==0):

    result.append(i)

print(f"Number is divisible by{m} and {n} are :{result}")
