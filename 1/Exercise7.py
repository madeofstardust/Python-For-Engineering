# Exercise7:
f = open("file.txt", "rU")
diction = {}
for line in f:
    x = line.split()
    diction[x[0]] = x[1]

print (diction)    