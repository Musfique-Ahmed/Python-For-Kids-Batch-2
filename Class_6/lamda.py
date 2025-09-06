square = lambda x: x**2

print(square(5))


def add(*args):
    return sum(args)

print(add(1,2,3,4,5))


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=25)