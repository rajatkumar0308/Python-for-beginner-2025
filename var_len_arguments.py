# *args and **kwargs allow you to pass a variable number of arguments to a function.
# They are very useful when you don't know in advance how many arguments a function might receive.

'''
1. *args (Non-Keyword Arguments)
Used to pass a variable number of non-keyword arguments to a function.
Inside the function, *args is treated as a tuple.
Features of *args:
Accepts multiple positional arguments.
The arguments are stored in a tuple.
You can iterate over them or access them using indexing. 
'''

# Summing Numbers
def sum_numbers(*args):
    total = sum(args)
    print(f"The sum is: {total}")

sum_numbers(1, 2, 3, 4, 5)

# Joining Strings
def join_strings(*args):
    result = " ".join(args)
    print(f"Joined string: {result}")

join_strings("Hello", "World", "Python", "is", "awesome")

#Accessing Arguments by Index
def print_args(*args):
    for i, value in enumerate(args):
        print(f"Argument {i}: {value}")

print_args(10, 20, 30, 40, 50)

'''
2. **kwargs (Keyword Arguments)
Used to pass a variable number of keyword arguments to a function.
Inside the function, **kwargs is treated as a dictionary.
Features of **kwargs:
Accepts multiple keyword arguments.
The arguments are stored in a dictionary.
You can iterate over keys and values.
'''
# Example 1: Displaying User Info
def display_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_user_info(name="John", age=30, location="New York")

# Example 2: Default Settings
def configure_settings(**kwargs):
    defaults = {"theme": "light", "font": "Arial", "autosave": True}
    defaults.update(kwargs)
    print("Current Settings:")
    for key, value in defaults.items():
        print(f"{key}: {value}")

configure_settings(theme="dark", autosave=False)

# Example 3: Combining with Regular Arguments
def print_details(name, age, **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details("Alice", 28, location="California", profession="Engineer")


#Combination of *args and **kwargs
#You can use both *args and **kwargs together in a single function. The order must always be:
#Regular arguments
#*args
#**kwargs
def full_details(greeting, *args, **kwargs):
    print(greeting)
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

full_details("Hello!", "Python", "is fun", language="Python", version="3.10")

