class MyClass:
    name="Mahesh"
    def sum(self,a,b):
        print(a+b)

x = MyClass()
print(x.name)
print(x.sum(10,20))

class MyClass:
    name="Mahesh"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sum(self,a,b):
        print(a+b)

x = MyClass("John", 40)
print(x.name)
x.sum(4,5)
print(x.age)
#del x
#print(x.age)
del x.name
print(x.age)