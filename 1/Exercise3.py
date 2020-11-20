# Exercise3:

def exchange(string1, string2):
    s1 = list(string1)
    s2 = list(string2)
    first_string1 = s1[0]
    first_string2 = s2[0]
    s1[0] = first_string2
    s2[0] = first_string1
    print ("First word changed: ", "".join(s1))
    print ("\n Second word changed: ", "".join(s2))
    
one, two = input().split()

exchange(one, two)