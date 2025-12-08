while True:
    user_number = 0
    try:
        user_number = int(input("Enter a number: "))
    except ValueError:
        print("Input is not a number.")
    try:
        10 / user_number
    except ZeroDivisionError:
        print("You can't divide by zero.")

    if user_number < 0:

        except NegativeNumberError:
            raise ("You can't use a negative number.")
