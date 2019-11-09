my_List = ["Tokyo", "London", "NewYork"]
print(my_List)
print(my_List[2])
for val in my_List:
    print(val)
print(len(my_List))
my_List.append("Bordon")
print(my_List)
my_List.insert(4,"Durham")
print(my_List)
my_List.remove("Tokyo")
print(my_List)
my_List.pop()
print(my_List)
my_List.pop(1)
print(my_List)
del my_List[1]
print(my_List)
my_List.clear()
print(my_List)

fruits = ["apples", "oranges", "cherry"]
print(fruits)
fruits.reverse()
print(fruits)

my_List2 = ["apples", 1, 2, 3.5]
my_List3 = ["apples", [1,2,3],['a','b','c']]
print(my_List3[1])
print(my_List3[1][1])