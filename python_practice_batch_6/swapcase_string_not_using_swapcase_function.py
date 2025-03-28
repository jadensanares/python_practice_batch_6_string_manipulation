# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# prompt user input
input_string = input("Enter the string: ")

# using simple loop for swap case without using swapcase() function
swapcase_string = ""
for character in input_string:
    if character.isupper():
        swapcase_string += character.lower()
    elif character.islower():
        swapcase_string += character.upper()
    else:
        swapcase_string += character

# print result