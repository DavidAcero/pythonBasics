# Methods: https://www.w3schools.com/python/python_dictionaries_methods.asp

myDict = {
    "name": "David",
    "city": "Ags",
    "age" : 27
}

print(myDict)
print(myDict["age"])
x = myDict.keys()
print(x)

myDict["gender"] = "Male"

x = myDict.keys()
print(x)
print(myDict)

# Update
myDict.update({"age": 25})
print(myDict)

myDict["name"] = "testName"
print(myDict)

# Add Items
myDict.update({"color": "Green"})
print(myDict)

myDict["lastName"] = "testLast"
print(myDict)