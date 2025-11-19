#Formated strings

template = "Dear {}, you are awesome. Take this ${} bag."

person_a = "John"
amount_a = 10000
person_b = "Jack"
amount_b = 1000
person_c = "Mary"
amount_c = 300

# This is the old way to do this previous to python 3.6
string = template.format(person_a, amount_a)
print(string)

print(f"Dear {person_b}, you are awesome. Take this ${amount_b} bag.")