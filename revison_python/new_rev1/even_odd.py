def decorator_one(func):
    def wrapper():
        func()
        print("Decorator One")
    return wrapper


def decorator_two(func):
    def wrapper():
        func()
        print("Decorator Two")
    return wrapper



@decorator_two
@decorator_one

def hello():
    print("Hello World!")
hello()


# a decorator is essentially a function that takes another function as input, adds some functionality and returns it.
# decorators are often used in scenario like logging enforcing address control , or measuring execution time