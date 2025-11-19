password = "1234"
does_password_match = False
user_input = input("Please enter Password: ")

while not does_password_match:
    if user_input == password:
        does_password_match = True
        print("Password Match")
    else:
        does_password_match = False
        user_input = input("Password Not Match, Please Try Again: ")