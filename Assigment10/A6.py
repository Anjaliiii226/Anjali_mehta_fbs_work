def remove(li):

    list = []

    for num in li:

         if num not in list :
                                                              
          list.append(num)

    return list
    

li = [10,30,10,30,10,40,70]

res = remove(li)       

print("Original list",li)

print("List after removing duplication",res)
    


        
