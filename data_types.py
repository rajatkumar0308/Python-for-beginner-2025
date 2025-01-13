#Variables
#A variable is a named location in memory used to store data.
#In Python, you don't need to declare a variable's type; 
#it is determined at runtime based on the value assigned.  
# Syntax ; variable_name = value


# Integer
age = 25
print("Age:", age)
print("Type:", type(age))

# Float
pi = 3.14159
print("Pi:", pi)
print("Type:", type(pi))

# String
name = "John Doe"
print("Name:", name)
print("Type:", type(name))

# Boolean
is_active = True
print("Is Active:", is_active)
print("Type:", type(is_active))

# List
#Definition: A list is an ordered, mutable collection of elements that allows duplicate values. #Key Characteristics:
#Ordered: Elements are stored in the order they are added.
#Mutable: You can change elements after creation (add, remove, modify).
#Duplicates: Allows duplicate elements and many data types can be in a list.
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print("Type:", type(fruits))
print("First fruit:", fruits[0])

# Tuple
#Definition: A tuple is an ordered, immutable collection of elements that allows duplicates. Like lists, elements can be of mixed data types, but once created, the elements cannot be changed.
#Key Characteristics:
#Ordered: Elements are stored in the order they are added.
#Immutable: You cannot modify the elements after creation.
#Duplicates: Allows duplicate elements.
coordinates = (10, 20, 30)
print("Coordinates:", coordinates)
print("Type:", type(coordinates))
print("First coordinate:", coordinates[0])

# Dictionary
#Definition: A dictionary is an unordered, mutable collection of key-value pairs, 
# ,where keys must be unique and immutable, while values can be of any data type and are mutable.
#Key Characteristics:
#Unordered (as of Python 3.6+, insertion order is preserved).
#Keys: Unique and immutable (e.g., strings, numbers, tuples).
#Values: Can be of any data type and are mutable.
#Used for mapping data to unique keys.
person = {"name": "Alice", "age": 30, "is_employed": True}
print("Person:", person)
print("Type:", type(person))
print("Name:", person["name"])

# Set
#Definition: A set is an unordered, mutable collection of unique elements. It is often used for operations like union, intersection, and difference.
#Key Characteristics:
#Unordered: Does not maintain any specific order of elements.
#Unique: Does not allow duplicate elements.
#Mutable: Elements can be added or removed, but items must be immutable (e.g., strings, numbers, tuples).
unique_numbers = {1, 2, 3, 3, 4}
print("Unique Numbers:", unique_numbers)
print("Type:", type(unique_numbers))
