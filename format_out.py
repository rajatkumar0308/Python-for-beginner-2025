# Formatting Output in Python

# Using str.format() - A versatile method for inserting variables into strings dynamically
name = "Alice"
age = 25
print("1. My name is {} and I am {} years old.".format(name, age))

# Using f-strings - A modern, concise, and faster way to embed expressions directly in strings (Python 3.6+)
name = "Bob"
age = 30
print(f"2. My name is {name} and I am {age} years old.")

# Controlling number formatting - Useful for rounding and displaying numbers to specific decimal places
pi = 3.141592653589793
print("3. Pi to 2 decimal places: {:.2f}".format(pi))  # Using str.format()
print(f"4. Pi to 3 decimal places: {pi:.3f}")          # Using f-strings

# Aligning text - Important for creating structured and aligned outputs, like tables or reports
print("{:<10} | {:^10} | {:>10}".format("Left", "Center", "Right"))  # Left, Center, and Right alignment
print(f"{'Left':<10} | {'Center':^10} | {'Right':>10}")

# Formatting numbers with commas - Enhances readability for large numbers by adding commas as thousand separators
large_number = 1234567890
print("5. Formatted number: {:,}".format(large_number))
print(f"6. Formatted number: {large_number:,}")

# Combining strings and variables dynamically - Useful for creating customized and meaningful outputs
item = "apple"
price = 0.5
quantity = 5
print(f"7. The total cost for {quantity} {item}s is ${price * quantity:.2f}.")
