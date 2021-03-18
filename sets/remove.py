# discard: don't raise an error if item dont exist
# remove : raise error if item dont exist

# Methods: https://www.w3schools.com/python/python_sets_methods.asp

thisSet = {"Australia", "Mexico", "Canada", "Russia" ,"Spain", "Egypt"}
print(thisSet)

thisSet.discard("Egypt")
print(thisSet)

thisSet.remove("Canada")
print(thisSet)

thisSet.clear()
print(thisSet)

del thisSet