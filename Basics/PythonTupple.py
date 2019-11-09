my_Tuple = ("Apples", "Oranges", "Grapes")
print(my_Tuple)
print(my_Tuple[1])
print(my_Tuple[-1])
print(my_Tuple[0:2])
for val in my_Tuple:
    print(val)
# my_Tuple[1] = "Cherry"
# my_Tuple[3] = "Cherry"
# del my_Tuple[2]
# del my_Tuple
print(len(my_Tuple))

my_Tuple2 = ("Banana", (1,2,3), ["Tokyo", "New Delhi"])
print(my_Tuple2)
print(my_Tuple2[2][1])
my_Tuple2[2][1] = "New York"
print(my_Tuple2)
print("Banana" in my_Tuple2)
print("Cherry" in my_Tuple2)