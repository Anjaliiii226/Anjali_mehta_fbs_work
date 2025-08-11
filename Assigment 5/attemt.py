correct_userid = "admin"
correct_password = "1234"

max_num = 3

for attempt in range(1, max_num + 1):
    
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")
    

    if userid == correct_userid and password == correct_password:
        print("Login Successful!")
        break
    else:
        print("Invalid User ID or Password.")
        
        if attempt < max_num:
            print(f"You have {max_num - attempt}:")
        else:
            print("Too many failed attempts. Access Denied!")