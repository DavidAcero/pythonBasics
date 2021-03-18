i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
else:
    print("DAVID")

print("=" * 30)

i = 1
while i < 6:
  print(i)
  i += 1
else:   # Only runs if no break on the loop
  print("i is no longer less than 6")