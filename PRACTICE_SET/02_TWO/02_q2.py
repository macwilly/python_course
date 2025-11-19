first_number = int(input("Please enter a number: "))
second_number = int(input("Please enter another number: "))
opr = input("Please enter a operator (+,-,*,/): ")

match opr:
    case "+":
        print(f"{first_number} + {second_number} = {first_number + second_number}")
    case "-":
        print(f"{first_number} - {second_number} = {first_number - second_number}")
    case "*":
        print(f"{first_number} * {second_number} = {first_number * second_number}")
    case "/":
        if second_number == 0:
            print("Cannot divide by zero")
        else:
            print(f"{first_number} / {second_number} = {first_number / second_number}")
    case _:
        print("Invalid operator")