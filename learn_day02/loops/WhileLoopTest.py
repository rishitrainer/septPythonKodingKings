'''
while condition:
    block of code when condition is true
    condition modifier
'''

# Add 1 to 10
# counter = 1 - condition - counter <= 10

counter = 1
total = 0
while counter <= 10:
    total = total + counter
    print("Counter Value :: ", counter)
    if counter == 6:
        break # Jump Out of Loop
    counter += 1 # counter+ 1 - condition modifier

print("Total of 1 to 10 ", total)