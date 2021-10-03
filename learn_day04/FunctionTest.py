'''
def method_name(input_parameters:optional):
    block of code
    return output: optional
1. input parameter is local variable in method
2. you can pass any number of parameters
3. Default Parameter value - kw parameters
4. Python can return multiple values
'''


def say_hello(lang, state="Maharashtra"):
    message = None
    if (lang == "English") and (state == "Maharashtra"):
        message = "Hello " + state
    else:
        message = "Namaste " + state
    return message, state

hello_msg,state = say_hello("English")
print(hello_msg, state)
hello_msg,state = say_hello("Hindi", "Goa")
print(hello_msg, state)
# <class 'function'>
print(type(say_hello))
