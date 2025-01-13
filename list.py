# Example codes demonstrating various list operations in Python

# 2. Create a list of numbers with a given range
# Generate a list of numbers from 1 to 10 using the range function
range_list = list(range(1, 11))
print("List of numbers from 1 to 10:", range_list)

# 3. Add list items
# Add single and multiple items to a list
my_list = [1, 2, 3]
my_list.append(4)  # Add single item
my_list.extend([5, 6])  # Add multiple items
print("List after adding items:", my_list)

# 4. How to add elements to a specific position in a list
# Use insert() to add an element at a specific index
my_list.insert(2, 99)  # Add 99 at index 2
print("List after inserting 99 at index 2:", my_list)

# 5. Python list access
# Access elements using their index
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# 6. List iteration operations
# Iterate over a list using a for loop
print("List elements:")
for item in my_list:
    print(item)

# 7. Python list search operations
# Check if an element exists in the list
search_item = 999
if search_item in my_list:
    print(f"{search_item} is in the list")
else:
    print(f"{search_item} is not in the list")

# 8. Python list remove operations
# Remove specific elements from a list
my_list.remove(99)  # Removes the first occurrence of 99
print("List after removing 99:", my_list)

# 9. Python list concatenation operations
# Concatenate two lists using + operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

# 10. Python list sorting and comparison
# Sort a list in ascending and descending order
unsorted_list = [3, 1, 4, 1, 5, 9]
unsorted_list.sort()  # Sort in ascending order
print("Sorted list (ascending):", unsorted_list)
unsorted_list.sort(reverse=True)  # Sort in descending order
print("Sorted list (descending):", unsorted_list)

# 11. Python unpack list
# Unpack list elements into variables
a, b, c = [1, 2, 3]
print("Unpacked values:", a, b, c)

# 12. Python list comprehension operations
# Create a new list using list comprehension
squared_list = [x**2 for x in range(1, 6)]
print("Squared list:", squared_list)

# 13. Python list reverse operations
# Reverse the elements of a list
original_list = [1, 2, 3, 4, 5]
original_list.reverse()
print("Reversed list:", original_list)

# 14. Python nested lists
# Create and access elements of a nested list
nested_list = [[1, 2, 3], [4, 5], [6]]
print("Nested list:", nested_list)
print("First sublist:", nested_list[0])
print("First element of the first sublist:", nested_list[0][0])

# 15. Python list flatten operation
# Flatten a nested list using list comprehension
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened_list)
