user_input = int(input("Please enter a number and I will till you if it is positive, negative or zero: \n"))
if user_input > 0:
    print(str(user_input) + " is positive")
elif user_input < 0:
    print(str(user_input) + " is negative")
else:
    print(str(user_input) + " is zero")