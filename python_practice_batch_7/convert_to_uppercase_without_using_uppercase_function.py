# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# Prompt user to input string
string_input = input("Enter the string :")

# Condition loop for converting the lowercase letters to uppercase letter without using the upper() function
uppercase_string = ""
for character in string_input:
    if 'a' <= character <= 'z':
        uppercase_string += chr(ord(character)) - 32)
    else:
        uppercase_string += character

# Print result