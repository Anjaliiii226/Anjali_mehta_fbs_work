for i in range(1,6):
    for j in range(1,7-i):
        print(' ',end =' ')
    for j in range(1 ,i+1):
        print(chr(64+j),end = ' ')
    for j in range(1,i):
        i+=1
        print(chr(64+i),end =' ')
    print()
    
