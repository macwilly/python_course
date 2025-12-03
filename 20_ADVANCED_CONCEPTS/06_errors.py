# For python try/except is used not try/catch
# Multiple types of exceptions can be handled
while True:
    try:
        a = int(input("Enter Number: "))
        b = int(input("Enter Number: "))
        print(f"The sum is {a+b}")
    except ValueError:
        print("Please enter a number.")
    except Exception as e:
        print(f"Invalid input: {e.args}")