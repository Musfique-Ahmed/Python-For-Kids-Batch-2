def greet(name):
    return f"Hello, {name}! How are you?"

def bye(name):
    return f"Bye Bye {name}, see you later!"


def factorial(number):
    prod = 1

    for i in range(1, number+1):
        prod *= i

    return prod