'''
String variables - "" or ''
'''

name = "David Burrow" # String
another_name = 'Neil Armstrong'
age = 55 # int
percentage = 99.14 # float
complex_var = 1 + 5j # complex
flag = False # boolean

print("name :: " , type(name), id(name))
print("another_name :: " , type(another_name), id(another_name))
print("age :: " , type(age), id(age))
print("percentage :: " , type(percentage), id(percentage))
print("complex_var :: " , type(complex_var), id(complex_var))
print("flag :: " , type(flag), id(flag))

float_age = float(age)
str_decimal = str(percentage)
print("Float age data type ", type(float_age))
print("percentage data type ", type(str_decimal))