# WHAT IS TUPLE ?

# A tuple is a collection in Python that’s ordered and immutable, meaning once you create it, 
# you can’t change its elements. 
# This makes tuples a great choice when you need to store data that shouldn’t be modified."

# Examples demonstrating various tuple operations in Python

# 1. Create a tuple
# Tuples are immutable sequences used to store a collection of items
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# 2. Access elements in a tuple
# Access elements by index
print("First element in tuple:", my_tuple[0])
print("Last element in tuple:", my_tuple[-1])

# 3. Iterate over a tuple
print("Elements in the tuple:")
for item in my_tuple:
    print(item)

# 4. Check if an element exists in a tuple
search_item = 3000
if search_item in my_tuple:
    print(f"{search_item} is in the tuple")
else:
    print(f"{search_item} is not in the tuple")

# 5. Concatenate tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# 6. Tuple slicing
# Extract portions of a tuple using slicing
sliced_tuple = my_tuple[1:4]
print("Sliced tuple (from index 1 to 3):", sliced_tuple)

# 7. Unpack tuple elements
a, b, c, d, e  = my_tuple
print("Unpacked values:", a, b, c, d, e )

# 8. Nested tuples
# Tuples can be nested just like lists
nested_tuple = ((1, 2), (3, 4, 5), (6,))
print("Nested tuple:", nested_tuple)
print("First sub-tuple:", nested_tuple[0])
print("First element of the first sub-tuple:", nested_tuple[0][0])

# 9. Tuple length
# Find the length of a tuple
print("Length of tuple:", len(my_tuple))

# 10. Count occurrences in a tuple
# Count how many times an element appears in a tuple
print("Count of 2 in tuple:", my_tuple.count(2))

# 11. Find index of an element in a tuple
# Find the index of the first occurrence of an element
print("Index of 4 in tuple:", my_tuple.index(4))

# 12. Tuple immutability
# Demonstrating immutability (will raise an error if uncommented)
#my_tuple[0] = 99  # TypeError: 'tuple' object does not support item assignment

# 13. Convert tuple to list and back
# Tuples can be converted to lists and vice versa
converted_list = list(my_tuple)
print("Tuple converted to list:", converted_list)
converted_tuple = tuple(converted_list)
print("List converted back to tuple:", converted_tuple)
