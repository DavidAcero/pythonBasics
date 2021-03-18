# Methods: https://www.w3schools.com/python/python_sets_methods.asp

thisSet = {"Australia", "Mexico", "Canada", "Russia" ,"Spain", "Egypt"}
print(thisSet)

thisSet.add("Taiwan")
print(thisSet)

thisSet.add("Australia")
print(thisSet)

anotherSet = {"Iceland", "Norway", "Finland"}
anotherList = ["Congo", "South Africa"]
thisSet.update(anotherSet)
thisSet.update(anotherList)
print(thisSet)