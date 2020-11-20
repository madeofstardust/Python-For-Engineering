# exercise8

f = open("file2.txt", "r")

data = f.read()
words = data.split()
diction = {}
print('Number of words in text file :', len(words))

words_sorted = sorted(words)
repetitions = []
previous = "?)(*"

for i in words_sorted:
    if i == previous:
        diction[i] += 1
    else:
        diction[i] = 1
        previous = i

print(diction)


