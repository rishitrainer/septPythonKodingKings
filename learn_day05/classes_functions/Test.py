def say_hello():
    print("Hello World")

say_hello()
print(type(say_hello))

greet = say_hello
greet()

def calculator(operation, number):
    # local functions
    def square():
        return number*number

    def cube():
        return number*number*number

    if operation == "square":
        return square
    else:
        return cube


value = calculator("cube", 5)
print(value())