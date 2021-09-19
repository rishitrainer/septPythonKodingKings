marks = [12,13,14,15,14,12]

'''
for eachSample in Collection:
    block of code for eachSample
'''
total = 0
for eachSubMarks in marks:
    total = total + eachSubMarks

print("Total Marks ", total)

# write same code in while loop
# range(endvalue) = 0 till endvalue -1
# range(start, end) ==> start till end -1
# range(start, end, step) ==> start till end -1 with step of provided value
# addition of 1 to 10 with for loop
sum = 0
for eachItem in range(1, 11):
    if eachItem == 6:
        continue
    print(eachItem)
    sum = sum + eachItem

print("Sum of 1 to 10 is ", sum )