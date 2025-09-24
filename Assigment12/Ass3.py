string = input("Enter a string: ")

if len(string) <= 1:
    print("New String:", string)   
   
    new_string = string[-1]   
    for i in range(1, len(string)-1):
        new_string += string[i]   

    print("Original String:", string)
    print("New String:", new_string)