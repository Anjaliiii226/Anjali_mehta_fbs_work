li = [10,30,50,70,70]
max = li[0]
min = li[0]
for i in range(1,len(li)):
    if(li[i]>max):
        max = li[i]
    if(li[i]<min):
        min = li[i]
print(f"mimimum number:",min )
print(f" maximum number :",max)