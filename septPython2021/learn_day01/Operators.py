import cmath

first = 9
second = 2
third = 10

# Mathematical Operator
print("Addition ", (first+second))
print("Subtraction ", (first - second))
print("Multiplication ", (first * second))
print("Division  ", (first / second))
print("Modulus / Reminder ", (first % second))
print("Rest to Power ", (first ** second))
print("Floor Div ", (first // second))
print(cmath.pi)

# Comparison > < >= <= != ==
print("Greater Than ", (first > second))
print("Greater Than or Equals ", (first >= second))
print("Less Than ", (first < second))
print("Less Than or Equals ", (first <= second))
print("Not Equal ", (first != second))
print("Equals ", (first == second))

# AND logic
'''
R = S1 and S2
S1  S2  R
T   T   T
T   F   F
F   T   F
F   F   F
T =1 F = 0 and = *
'''
first = 9
second = 2
third = 10

S1 = first > second # T
S2 = first > third # F
and_result = S1 and S2
or_result = S1 or S2
print("and_result " , and_result)
print("or_result " , or_result)
# or logic
'''
R = S1 or S2
S1  S2  R
T   T   T
T   F   T
F   T   T
F   F   F
T =1+ F = 0 or = +
'''

'''
Negation not
R = not S1
S1  R
T   F
F   T
'''
print(not True)
print(not False)