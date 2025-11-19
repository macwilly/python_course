from unittest import case

user_input = int(input("Enter a number 1-7 and I will say the day of the week 1= Monday 7 = Sunday: "))

match user_input:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Please enter a number between 1 and 7")