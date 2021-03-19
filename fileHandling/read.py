# Read Entire File
f = open("fileHandling/readExample.txt", "r")
print(f.read())

print("=" * 30)

# Read part of the file
f = open("fileHandling/readExample.txt", "r")
print(f.read(12))

print("=" * 30)

# Read first line of the file
f = open("fileHandling/readExample.txt", "r")
print(f.readline())

print("=" * 30)

# Read each line of the file
f = open("fileHandling/readExample.txt", "r")
for line in f:
    print("Line: {}".format(line),end='')
print('\n')

print("=" * 30)

# Read first as a list
f = open("fileHandling/readExample.txt", "r")
print(f.readlines())

f.close()