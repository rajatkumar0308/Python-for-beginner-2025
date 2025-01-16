
# Arithmetic Operators Example
a = 10
b = 3

print("Addition:", a + b)       # Output: 13
print("Subtraction:", a - b)    # Output: 7
print("Multiplication:", a * b) # Output: 30
print("Division:", a / b)       # Output: 3.333...
print("Modulus:", a % b)        # Output: 1
print("Exponentiation:", a ** b) # Output: 1000
print("Floor Division:", a // b) # Output: 3

# Comparison Operators Example
x = 5
y = 8

print("Equal to:", x == y)        # Output: False
print("Not equal to:", x != y)    # Output: True
print("Greater than:", x > y)     # Output: False
print("Less than:", x < y)        # Output: True
print("Greater than or equal:", x >= y) # Output: False
print("Less than or equal:", x <= y)    # Output: True
#--------------------------------------------------------------------------------------------------------------#

# Logical Operators Example
a = True
b = False

print("AND:", a and b)  # Output: False
print("OR:", a or b)    # Output: True
print("NOT:", not a)    # Output: False

# Assignment Operators Example
x = 10
print("Initial value of x:", x)

x += 5  # Add and assign
print("After x += 5:", x)  # Output: 15

x -= 3  # Subtract and assign
print("After x -= 3:", x)  # Output: 12

x *= 2  # Multiply and assign
print("After x *= 2:", x)  # Output: 24

x /= 4  # Divide and assign
print("After x /= 4:", x)  # Output: 6.0

# Membership Operators Example
fruits = ['apple', 'banana', 'cherry']
print("Is 'apple' in fruits?", 'apple' in fruits)  # Output: True
print("Is 'grape' not in fruits?", 'grape' not in fruits)  # Output: True


# Identity Operators Example
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is y:", x is y)       # Output: False (different objects)
print("x == y:", x == y)       # Output: True (same values)
print("x is z:", x is z)       # Output: True (same object)

# Bitwise Operators Example
a = 5  # Binary: 0101
b = 3  # Binary: 0011

print("Bitwise AND:", a & b)  # Output: 1 (Binary: 0001)
print("Bitwise OR:", a | b)   # Output: 7 (Binary: 0111)
print("Bitwise XOR:", a ^ b)  # Output: 6 (Binary: 0110)
print("Bitwise NOT:", ~a)     # Output: -6 (Binary: Inverted 1010)
print("Left Shift:", a << 1)  # Output: 10 (Binary: 1010)
print("Right Shift:", a >> 1) # Output: 2 (Binary: 0010)
