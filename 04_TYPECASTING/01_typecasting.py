# Typecasting  is the processing of changing one object type into another. Such as an int into a string

int_a = 34
string_b = "34"

print(int_a)
print(type(int_a))
print(string_b)
print(type(string_b))

# Convert string_b to an integer
int_b = int(string_b)

print(int_b)
print(type(int_b))

string_a = str(int_a)
print(string_a)
print(type(string_a))

float_a = float(int_a)
print(int_a)
print(type(float_a))

bool_a = bool(int_a)
print(bool_a)
print(type(bool_a))

float_c = 3.14159
print(float_c)
print(type(float_c))

# Changing a float to an int will just floor the number
int_c = int(float_c)
print(int_c)
print(type(int_c))