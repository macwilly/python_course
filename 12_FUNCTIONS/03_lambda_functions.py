# Lambda functions are anonymous in line functions similar in concept to JavaScript arrow function ()=>
# Can be used to pass a function to a function.
square = lambda num: num * num
sum = lambda num1, num2: num1 + num2

print(square(5))
print(sum(10, 20))

def add(num1, num2):
    return num1 + num2