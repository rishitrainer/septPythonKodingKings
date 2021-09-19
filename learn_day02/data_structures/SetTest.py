'''
Set: Unordered, No Duplicates
{} Sets are written with curly brackets

'''
# Sets are written with curly brackets
sampleSet = {"apple", "banana", "strawberry", "crustedApple"}
anotherSet = { "tomatos", "potatos", "mango", "Carrot"}
print(sampleSet)
# Add Element: sampleSet.add("mango")
sampleSet.add("mango")
sampleSet.add("mango")
sampleSet.add("mango")
print(sampleSet)
# Iterate: for eachItem in sampleSet:


# Element Exists? : if "apple" in sampleSet:


# Add another set: sampleSet.update(anotherSet)
sampleSet.update(anotherSet)
print(sampleSet)

# Check Length: len(sampleSet)

# Remove Element: sampleSet.remove("banana")
# sampleSet.remove("blueberry")

# Discard (No Error) : sampleSet.discard("apple")
sampleSet.discard("blueberry")

# Clear Set: sampleSet.clear()
