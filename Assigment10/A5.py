def number(li,num):
    if(num in li):
        return True
    else:
        return None 
li = [10,40,67,89,90]
n = int(input("Enter the number:"))
count = li.count(n)
res = number(li,n)
if(res):
    print(f"Element present in list",{count})
else:
    print(f"Elements not present in list")