# newlist = [expression for item in iterable if condition == True]
countries = ["Australia", "Mexico", "Canada", "Russia", "US" ,"Spain", "Egypt"]
newList = [x for x in countries if "a" in x]    # add x for every x in countries if 'a' appears on x
print(newList)

anotherList = [x for x in range(10)]
print(anotherList)

# Return the item if it is not Russia, if it is Russia return orange
anotherList = [x if x != "Russia" else "Orange" for x in countries] 
print(anotherList)