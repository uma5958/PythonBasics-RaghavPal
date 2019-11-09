my_Set = {"Chalk", "Duster", "Board"}
print(my_Set)
for val in my_Set:
    print(val)

print("Chalk" in my_Set)
my_Set.add("Pen")
print(my_Set)
# my_Set.add(['Pencil', 'Eraser'])
#print(my_Set)
print(len(my_Set))
my_Set.remove("Duster")
print(my_Set)
my_Set.discard("Pen")
print(my_Set)
# my_Set.remove("Duster")
my_Set.discard("Pen")

my_Set.pop()
print(my_Set)
my_Set.clear()
print(my_Set)
del my_Set

my_Set2 = {"Apple", 1, 2, (3,4,5)}
print(my_Set2)

my_List = [1, 2, 3]
print(my_List)
my_Set3 = set(my_List)
print(my_Set3)

# Union | Intersection | Diff | Symmetric
A = {'A', 'B', 1, 2, 3}
B = {'B', 'C', 3, 4, 5}

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)

print(A.symmetric_difference(B))
print(A ^ B)

