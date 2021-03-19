import os
if os.path.exists("fileHandling/deleteExample.txt"):
  os.remove("fileHandling/deleteExample.txt")
else:
  print("The file does not exist")