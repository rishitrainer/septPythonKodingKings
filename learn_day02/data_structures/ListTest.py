'''
1. Ordered - index
2. Allows duplicates
3. []
index starts with 0
'''
# Lists are written with square brackets.
sampleList = ["apple", "banana", "strawberry", "crustedApple"]
# Access Items: sampleList[1]
print(sampleList[1])
# Add Element: sampleList.append("newItem")
sampleList.append("blueberry")
sampleList.append("blueberry")
sampleList.append("blueberry")
print(sampleList)
# Add Indexed Element: sampleList.insert(1, "fruits")
sampleList.insert(1, "jackfruit")
print(sampleList)
# Remove Element: sampleList.remove("item")
sampleList.remove("blueberry")
print(sampleList)
# Remove Indexed Element: sampleList.pop(1)
sampleList.pop(1)
print(sampleList)
# Using Delete function: del sampleList[0]

# Check the Length: len(sampleList)
print(len(sampleList))
# Iterate: for eachItem in sampleList:
for eachFruit in sampleList:
    print(eachFruit)

# Element Exists membership ? : if "apple" in sampleList:

if "apple" in sampleList:
    print("Apple exists")

#Sorting: sampleList.sort() - can you sort in descending order - ?
sampleList.sort()
print(sampleList)
sampleList.reverse()
print(sampleList)

# Clear List: sampleList.clear()
sampleList.clear()
print(sampleList)