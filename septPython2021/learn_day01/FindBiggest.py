first = int(input("Enter First Number:: "))
second = int(input("Enter Second Number:: "))
third = int(input("Enter third number:: "))
fouth = int(input("Enter Fourth number:: "))

big = first > second
print("First > Second ", big)

'''
Flow Controls 
if condition:
    block of code when condition is true
else:
    block of code when condition is false
'''

if first > second :
    print("First Number is Greater")
    print("First Number is ", first)
elif second > first:
    print("Second NUmber is Greater")
    print("Second Number is ", second)
else:
    print("Both are equal")

'''
first > second and first > third 
    - first
second > third
    - second
third
'''
if (first > second) and (first > third):
    print("First is Greater ", first)
elif second > third:
    print("Second is Greater ", second)
else:
    print("Third is Greater ", third)

# Find Biggest number from Fourth number