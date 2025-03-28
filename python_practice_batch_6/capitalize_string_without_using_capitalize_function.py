# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# prompt user input
input_string = input("Enter the string: ")

# capitalization of first letter of the string
if input_string:
    capitalized_string = input_string[0].upper() + input_string[1:].lower()
else:
    capitalized_string = ""

# print result
