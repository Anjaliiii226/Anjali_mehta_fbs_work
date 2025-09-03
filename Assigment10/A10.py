li = [10,20,40,50,50,60,40,70,10]

n = int(input("Enter the number :"))

list =[]

for num in li :

    if num!= n:

     list.append(num)

print("Original number",li)
print("List of removing all occurence of given number",n ,list)