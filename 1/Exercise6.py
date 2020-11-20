# exercise6:
list_numbers = input().split()

previous = "a"
repetitions = []
for i in list_numbers:
    if i == previous:
        repetitions.append(i)
    else:
        previous = i

for i in repetitions:
    for n in list_numbers:
        if i == n:
            list_numbers.remove(n)
            continue
        
print(list_numbers)
    