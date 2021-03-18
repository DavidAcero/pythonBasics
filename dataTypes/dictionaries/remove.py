# Methods: https://www.w3schools.com/python/python_dictionaries_methods.asp
myDict = {
    "name": "David",
    "city": "Ags",
    "age" : 27
}

myDict.pop("age")
print(myDict)

del myDict["city"]
print(myDict)

myDict.clear()
print(myDict)

del myDict