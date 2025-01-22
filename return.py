'''The return statement in Python is used to send a result from a function to the caller. 
It immediately exits the function, optionally passing back a value.'''

# Function to calculate the square of a number
def calculate_square(number):
    return number * number

# Calling the function
result = calculate_square(5)
print("The square is:", result)


# Function to analyze a list of numbers and return multiple values
def analyze_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    max_number = max(numbers)
    min_number = min(numbers)
    return total, average, max_number, min_number

# Calling the function
numbers = [10, 20, 30, 40, 50]
total, average, max_number, min_number = analyze_numbers(numbers)

print("Total:", total)
print("Average:", average)
print("Max number:", max_number)
print("Min number:", min_number)
