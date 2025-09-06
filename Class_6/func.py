# Defining a function
def my_func():
    print("Print Hello World!")

# Calling the function
my_func()


def my_func(message):
    print(message)

my_func("Hi, Hello!")


def sume(x, y):
    sum = x+y

    return sum

print(sume(4,6))



lst = [1,2,3,4,5,6,7]


print(len(lst))


print(len("nusaybah"))



def my_fanc():
    print("nusaybah")
my_fanc()


def greet(name):
    print(f"Hi, {name}. How are you?")

greet("nusaybah")
greet("musfique")
greet("ahmed")
greet("tasnia")
greet("ripa")



def do(num):
    sum=num**2
    return sum

print(do(3))



def greet(name="guest"):
    print(f"Hi, {name}. How are you?")
greet()
greet("anik")



def tri(uchota,vumi = 4):
    area = .5 * vumi * uchota

    return area

print(tri(5))
print(tri(5, 6))

