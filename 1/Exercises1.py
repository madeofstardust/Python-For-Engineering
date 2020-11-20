#Exercises 1, 24.02
#Ex1.
import sys
try: 
    name = sys.argv[1]
except:
    print("Oops! There is no arg passed. Try again!")
    exit()
'''
if name == 'Weronika' or 'Nika':
    print("Hi, Princess")
else:
    print ("Who are You? o.O")
   ''' 
    
if int(name) <=9:    
    print("The number of cookies is", name)
else:
    print("Too many cookies!")