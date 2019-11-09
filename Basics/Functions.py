def printHello():
    print("Hello")
printHello()

def printHi(name="John"):
    print("Hi, "+name)
print(printHi())
printHi("Mahesh")

def sum(a,b,c):
    print("Sum is: ",a+b+c)
sum(10, 20, 30)

def returnSum(a,b):
    '''This function returns the sum of given numbers'''
    """Based on given input it returns the sum of given input"""
    return (a+b)
x = returnSum(10,20)
print("Sum returned is: ",x)
