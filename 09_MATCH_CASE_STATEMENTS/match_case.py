# This was introduced to Python in 3.10 so it is relatively new to Python
# bottom line this is a switch statement, but you use match instead of switch
# Note that the default case is not default but 'case _:'
# Note case stacking is with a '|'


a = int(input("Enter a number:\n"))

match a:
    case 1 | 2:
        print("we are in case 1")
    case 34:
        print("we are in case 34")
    case _:
        print("we are in case default")
