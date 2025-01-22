'''Lambda Functions in Python
A lambda function is an anonymous, single-line function defined using the lambda keyword. 
It can have any number of input arguments but only one expression, which is evaluated and returned. 
Lambda functions are often used for short, throwaway operations, making code concise.'''

#Key Points about Lambda Functions:
#Syntax: lambda arguments: expression
#They don’t have a name; often used where functions are required temporarily.
#Useful with higher-order functions like map(), filter(), and reduce().
#Can be assigned to variables or passed directly as arguments.
#Limited to a single expression (no multi-line functionality).

# Function to calculate the square of a number
square = lambda x: x * x
print(square(5))  # Output: 25

# Function to calculate the sum of two numbers
sum_two_numbers = lambda x, y: x + y
print(sum_two_numbers(10, 15))

# Function Double each number in a list
numbers = [1, 2, 3, 4, 5]
#map() is a Python built-in function that applies a given function to all items in an input iterable.
#In this case, the iterable is numbers.
#The function being applied is lambda x: x * 2
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

# Function Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
#filter() is a Python built-in function used to filter elements of an iterable based on a condition.
#It takes two arguments: a function and an iterable.
#The function is applied to each element of the iterable, 
# and only elements for which the function returns True are included in the result.
print(evens)  # Output: [2, 4, 6]


# Function to Find the product of all numbers in a list
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
# The reduce() function in Python is a part of the functools module and is used to apply a function cumulatively 
# to the items of an iterable, reducing the iterable to a single value
print(product)  # Output: 24

# Sort a list of tuples by the second element
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
# The key parameter expects a function that takes one argument and returns the value to sort by.
''' lambda x: x[1] is an anonymous function
 Takes a tuple x as input.
 Returns the second element (x[1]) of the tuple'''
print(sorted_pairs)  # Output: [(4, 1), (2, 2), (1, 3)]



