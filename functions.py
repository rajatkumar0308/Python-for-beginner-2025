#What is a Python Function?
#A function in Python is a block of reusable code that performs a specific task. Functions help in reducing redundancy, improving readability, and organizing the code. Python provides two types of functions:

#Built-in functions (e.g., print(), len())
#User-defined functions (created by the programmer using the def keyword).
#def function_name(parameters):
#    """Docstring (optional): Describes the function."""
#      Function body
#    return value  # (optional) returns a result

#User-Defined Functio
def greet(name):
    """This function greets the person by name."""
    print(f"Hello, {name}! Welcome to Python.")
    
# Calling the function
greet("Rajat")

#Functions with Keyword Parameters
def introduce(name, age):
    """Introduce a person with their name and age."""
    print(f"My name is {name} and I am {age} years old.")
    
# Calling the function using keyword arguments
introduce(age=25, name="Bob")
introduce(age=250, name="Sitaram")


#Functions with Default Parameters
def greet_user(name, greeting="Hello"):
    """Greet the user with a customizable greeting."""
    print(f"{greeting}, {name}!")
    
# Calling the function with and without the default parameter
greet_user("Alice")               # Uses the default greeting
greet_user("Bob", "Good morning")  # Customizes the greeting

