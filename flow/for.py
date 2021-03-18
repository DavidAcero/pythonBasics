fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("=" * 30)

for x in "banana":
  print(x)

print("=" * 30)

for x in fruits:
  print(x)
  if x == "banana":
    break

print("=" * 30)

for x in fruits:
  if x == "banana":
    continue
  print(x)

print("=" * 30)

for x in range(2, 30, 3):
  print(x)
  
print("=" * 30)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("=" * 30)

for x in [0, 1, 2]:
  pass