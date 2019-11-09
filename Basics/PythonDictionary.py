my_Dict = {"class" : "animal", "name" : "giraffe", "age" : 10}
print(my_Dict)
print(my_Dict["name"])
print(my_Dict.get("name"))
print(my_Dict.values())

for x in my_Dict:
    print(x)

for x in my_Dict:
    print(my_Dict[x])

for x,y in my_Dict.items():
    print(x,y)

my_Dict["name"] = "elephant"
print(my_Dict)

my_Dict["color"] = "grey"
print(my_Dict)

my_Dict.pop("color")
print(my_Dict)

my_Dict.popitem()
print(my_Dict)

del my_Dict["class"]
print(my_Dict)

my_Dict.clear()
print(my_Dict)

del my_Dict