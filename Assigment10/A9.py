li = [1,2,34,5,6,7,8,9,10]
even = []
odd = []

for i in range(0,len(li)):
 if(i%2==0):
    even.append(li[i])
 elif(i%2!=0):
   odd.append(li[i])

print("Even number is ",even)
print("Odd number is",odd)

