sampleDictionary = {
    "model" : "Ertiga",
    "make" : "Maruti",
    "Year" : 2021,
    "Passing" : "JH",
    "state" : "JH",
}

print(sampleDictionary)
# Accessing Items: sampleDictionary["101"]
print(sampleDictionary["model"])
print(sampleDictionary.get("model"))
sampleDictionary["color"] = "Gray"
print(sampleDictionary)
sampleDictionary["Passing"] = "GJ"
print(sampleDictionary)

for eachKey in sampleDictionary:
    print(eachKey, sampleDictionary.get(eachKey))
# sampleDictionary.items()
for key, value in sampleDictionary.items():
    print(key, value)

for eachValue in sampleDictionary.values():
    print(eachValue)

# Remove Item with Key: sampleDictionary.pop("101")
sampleDictionary.pop("Passing")
print(sampleDictionary)
sampleDictionary.popitem() # recent insert will be removed
print(sampleDictionary)
print(len(sampleDictionary))
sampleDictionary.clear()
print(sampleDictionary)



