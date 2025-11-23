VALID_USERNAME = "admin"
VALID_PASSWORD = "12345"

def login_system():
    print("---- Login System ----")
    
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        print("\n✅ Login Successful! Welcome,", username)
    else:
        print("\n❌ Login Failed! Incorrect username or password.")

login_system()
