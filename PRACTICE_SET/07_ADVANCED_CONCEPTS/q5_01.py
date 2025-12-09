class NegativeNumberError(Exception):
    pass


try:
    user_number = int(input("Enter a number: "))

    if user_number < 0:
        raise NegativeNumberError("You can't use a negative number.")
    result = 10 / user_number
    print("The result is: ", result)

except ValueError:
    print("Input is not a number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
except NegativeNumberError as e:
    print(e)
