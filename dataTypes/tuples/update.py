'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''

countries = ("Australia", "Mexico", "Canada", "Russia", "US" ,"Spain", "Egypt")

print("Before Update: {}".format(countries))
workaround = list(countries)
workaround.extend(["France", "Germany", "Italy", "Japan", "China"])
countries = tuple(workaround)

print("After Format:  {}".format(countries))

workaround = list(countries)
workaround.remove("Spain")
countries = tuple(workaround)
print("After Format:  {}".format(countries))

del countries