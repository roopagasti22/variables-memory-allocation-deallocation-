def validate_user(username, password):
    return username == "Admin" and password == "python123"


username = input("Enter username: ")
password = input("Enter password: ")

if validate_user(username, password):
    print("Valid user")
else:
    print("Invalid user")