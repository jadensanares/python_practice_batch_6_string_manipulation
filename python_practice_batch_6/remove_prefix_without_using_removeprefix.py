# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter.
# Create a program that do the same functionality without using removeprefix() function.

# Ask the user for input
user_input = input("Enter a string: ")

# Ask the user to enter a prefix to remove
prefix = input("Enter prefix to remove: ")

# Make a condition for if the string starts with or without a prefix
if user_input[:len(prefix)] == prefix:
    cut_string = user_input[len(prefix):]
else:
    cut_string = user_input

# Print Result