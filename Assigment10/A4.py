li = [10,30,50,60,90]
max = li[0]
smax=0
for i in range(1,len(li)):
    if(li[i]>max):
        smax = max
        max = li[i]
    elif(li[i]>smax):
        smax = li[i]
print("maximum number is",max)
print("Second maximum number is",smax)