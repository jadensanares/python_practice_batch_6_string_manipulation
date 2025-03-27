# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# Tell the user to enter a string with leading spaces
user_input = input("Enter a string with leading spaces: ")

# Make an index of the first non-space character
index = 0
while index < len(user_input) and user_input[index] == " ":
    index += 1

# Cut the string from the non-space character
removed_string = user_input[index]

# print result
print("Removed leading space string:", removed_string)