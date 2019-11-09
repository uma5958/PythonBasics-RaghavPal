# ifelse-if
if 5>3:
    print("5 is greater than 3")
num = 0
if num>0:
    print("This is positive number")
elif num==0:
    print("number is zero")
else:
    print("This is a nagative number")

# for loop
num = [1,2,3,4,5]
for val in num:
    print(val)

num = [1,2,3,4,5]
sum = 0
for val in num:
    sum=sum+val
print("Total is: ",sum)

# for-else combination
fruits = ["apple", "oranges", "grapes"]
for val in fruits:
    print(val)
else:
    print("No fruits left")

# while loop
# num = 10
print("Enter a number: ")
num = int(input())
sum = 0
i=1
while i<num:
    sum=sum+i
    i=i+1
print("Total is: ",sum)

