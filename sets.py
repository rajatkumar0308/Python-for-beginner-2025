
#Sets are used to store multiple items in a single variable.
#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary.
#A set is a collection which is unordered, unchangeable*, and unindexed.

# Access Set Items
# Sets allow checking the existence of an item with `in`.
my_set = {1, 2, 3, 4}  
print(30 in my_set)  # Output: True if 3 exists in the set, otherwise False.

# Add Set Items
# Sets allow adding new elements using the `add` method.
my_set.add(5)  
print(my_set)  # Output: The set with the new element added.

# Remove Set Items
# You can remove an item from a set using `remove`. 
# Note: If the item doesn't exist, it raises a KeyError.
my_set.remove(2)  
print(my_set)  # Output: The set after the element is removed.

# Loop Sets
# Looping through a set to access each element individually.
for item in my_set:
    print(item)  # Output: Each item in the set printed one by one.

# Join Sets
# Sets can be joined using `union`, which combines all unique items from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
joined_set = set1.union(set2)  
print(joined_set)  # Output: A new set containing all unique elements.

# Set Methods
# Intersection finds common elements between two sets.
print(set1.intersection(set2))  # Output: {3}, as it is the only common element.

# Difference finds elements in the first set but not in the second.
print(set2.difference(set1))  # Output: {1, 2}, as they are unique to set1.

# Set Exercises
# Adding a new item to the set.
set3 = {10, 20, 30}
set3.add(40)  

# Discarding an item removes it without raising an error if it doesn't exist.
set3.discard(10)  

# Printing the modified set.
print(set3)  # Output: The final set after additions and removals.
