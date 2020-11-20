# Exercise 4:

myList = input().split()
counter = 0
for i in myList:
    if ((len(i) > 2) and (i[0] == i[-1])):
        counter +=1
        
print(counter)


    