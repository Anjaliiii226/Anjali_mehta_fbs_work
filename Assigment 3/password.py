userid = input("Enter User ID: ")
password = input("Enter Password: ")


if userid == correct_userid and password == correct_password:
    print(" Login Successful!")
else:
    print(" Invalid User ID or Password.")