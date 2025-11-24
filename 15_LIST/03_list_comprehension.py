# Create a list containing the table of 5

a= 5
table = []
for i in range(1,11):
    table.append(a*i)

print(table)

# In a list you can also do calculations and run loops to create the value this will only work for a single line in loop
table_two = [a*i for i in range(1,11)]
print(table_two)

table_three = [f"Lets count {i}" for i in range(1,11)]
print(table_three)