print("Hello world")
# Case sensitive, Latters(a-z), underscore, numbers(0-9)
x = 5
y = "Automation"
print(x)    # 5
print(y)    # Automation
print("Hello "+y)   # Hello Automation

x = 10
y = 20
print(x+y)  # 30

if 10 > 5:
    print("10 is greater than 5")

def sum(a, b):
    print(a+b)
x = sum(10, 20)

x = 5
y = 2.5
z = 4j
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# Casting
x = int(2)
y = int(2.5)
z = float(1)
p = str("10")
print(x)    # 2
print(y)    # 2
print(z)    # 1.0
print(p)    # 10

# Strings
x = "Hello world..."
print(x)
print(x[1])
#print(x[6, 11])
print(len(x))
print(x.lower())
print(x.upper())

x1 = " Hello world... "
print(x1)
print(x1.strip())
print(x1.replace("e","a"))

x2 = "Hello,World"
print(x2.split(","))

print("Enter your name: ")
x = input()
print("Hello "+x)
