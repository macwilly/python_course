# A Way to assign a value to an operator with an expression
def very_slow_function():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70

#a = very_slow_function()
# the walrus operator will assign the function return to the variable
# if((a:=very_slow_function())> 10):
#     print(a)
# else:
#     print("Not greater")


while(data:=input("Enter the value: ")):
    print(data)
    if data == 'q':
        print("Goodbye")
        break


