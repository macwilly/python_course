# Raising the exception will cause the program to crash 
while True:
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    if b == 0:
        raise ValueError("Please don't divide by zero.")

    print(f"The product is {a/b}")