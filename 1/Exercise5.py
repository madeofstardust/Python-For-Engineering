# Exercise5:

input_list = input().split()

my_list = []

for i in input_list:
    if i[0] == 'x':
        my_list.append(i)
        
print(sorted(my_list))



