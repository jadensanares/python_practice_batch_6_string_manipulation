# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# Ask the user to enter a string
user_input = input("Enter a string: ")

# Make an empty string to store lowercase outcome
lowercase_string = ""

# Make a loop for each character in the string
for character in user_input:
    if "A" <= character <= "Z":   # Condition to ehck if the character is either lowercase or uppercase
        lowercase_string += chr(ord(character) + 32)  # Conversion of upper to lowercase
    else:
        lowercase_string += character

# Print result
