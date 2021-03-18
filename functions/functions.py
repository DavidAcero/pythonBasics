def sayHello(fName, lName):
    print("Hello " + fName + " " + lName)

def anotherHello(*names):  # Use * if we dont know how many arguments we'll get
    print("Hello " + names[0] + " " + names[1])

def getInfo(**info): # Use ** if you dont know how many keyword arguments you'll get
    print("Age: {}".format(info['age']))
    print("Number: {}".format(info['number']))

def myCountry(country = "Mexico"):
    print("I'm from " + country)

def myReturn(x):
    return 5*x

sayHello("David", "Acero")

print("=" * 30)

anotherHello("David", "Acero")

print("=" * 30)

getInfo(age=24, number="12344")

print("=" * 30)

myCountry()

print("=" * 30)

myCountry("Brasil")

print("=" * 30)

number = myReturn(8)
print(number)


## RECURSION
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print("Result: {} K: {} Function: {}".format(result, k, result - k))
  else:
    result = 0
  return result

print("\nRecursion Example Results")
tri_recursion(6)
