#  A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

print("=" * 30)

# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

print("=" * 30)

# Use lambda functions when an anonymous function is required for a short period of time.

def myfunc(n):
    if n > 10 :
        return lambda a : a + n
    else:
        return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(15)

print(mydoubler(11))
print(mytripler(11))