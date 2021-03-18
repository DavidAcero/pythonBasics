countries = ["Australia", "Mexico", "Canada", "Russia", "US" ,"Spain", "Egypt"]
otherCountries = ["Congo", "El Salvador", "Denmark"]
countries[2] = "New Zeland"
print(countries)

countries.insert(4, "France")
print(countries)

countries.append("South Africa")
print(countries)

countries.extend(otherCountries)
print(countries)

countries.remove("El Salvador")
print(countries)

countries.pop(2) # Remove Third element
print(countries)

countries.pop() # Remove Last element
print(countries)

del countries[3]
print(countries)