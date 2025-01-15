# Python input() Function --> The input() function allows user input.

# Example 1: Basic Input
# Prompting the user to enter their name.
name = input("Enter your name: ")
print("Hello, " + name + "!")  # Greeting the user.

# Example 2: Input with Type Conversion
# Prompting the user to enter their age.
age = int(input("Enter your age: "))
years_to_100 = 100 - age  # Calculating years to reach 100.
print("You will turn 100 in " + str(years_to_100) + " years!")

# Example 3: Input for Multiple Values
# Prompting the user to enter three numbers separated by spaces.
numbers = input("Enter three numbers separated by spaces: ").split()
num1, num2, num3 = map(int, numbers)  # Converting inputs to integers.
print("The sum of the numbers is:", num1 + num2 + num3)  # Displaying the sum.

# Example 4: Input with Conditional Logic
# Prompting the user to guess a predefined number.
secret_number = 7
guess = int(input("Guess the secret number (1-10): "))
if guess == secret_number:
    print("Congratulations! You guessed it right.")
else:
    print("Sorry, that's not correct. The secret number was", secret_number)
