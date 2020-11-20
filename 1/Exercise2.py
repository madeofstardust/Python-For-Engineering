# Ex2:
myString = input("Input sth: \n")

def removal(someString):
    someString = someString[1:]
    someString = someString[:-2]
    print(someString)
    
removal(myString)
