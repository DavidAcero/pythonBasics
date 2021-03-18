thisSet = {"Amsterdam", "Berlin", "Chicago", "Dublin", True, 62, "London"}
anotherSet = set(("Amsterdam", "Berlin", "Chicago", "Dublin", True, 62, "London"))
print(thisSet)
print(anotherSet)

for i in anotherSet:
    print(i)

if "Berlin" in anotherSet:
    print("Berlin is in the set.")