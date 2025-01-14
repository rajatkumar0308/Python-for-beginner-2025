# Dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates

# Access Items: Accessing a value using a key
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Output: Alice

# Change Items: Modifying a value for a specific key
my_dict["age"] = 30
print(my_dict)  # Output: {'name': 'Alice', 'age': 30}

# Add Items: Adding a new key-value pair
my_dict["city"] = "New York"
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Remove Items: Removing a key-value pair
my_dict.pop("age")
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}

# Loop Dictionaries: Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# city: New York

# Copy Dictionaries: Creating a shallow copy of the dictionary
copied_dict = my_dict.copy()
print(copied_dict)  # Output: {'name': 'Alice', 'city': 'New York'}

# Nested Dictionaries: Creating a dictionary with nested dictionaries
nested_dict = {
    "child1": {"name": "Tom", "age": 10},
    "child2": {"name": "Jerry", "age": 8}
}
print(nested_dict["child1"]["age"])  # Output: Tom

# Dictionary Methods: Using the get() method
print(my_dict.get("name"))  # Output: Alice

# Dictionary Exercises: Check if a key exists
if "Name" in my_dict:
    print("Key exists!")  # Output: Key exists!
else:
    print("Key does not exist!")
