# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# prompt the user for the input
string_input = input("Enter the string: ")
suffix = input("Enter the suffix that will be removed: ")

# make the conditions for checking if the strings ends with the provided suffix
if string_input.endswith(suffix):
    trimmed_string = string_input[: -len(suffix)]
else:
    trimmed_string = string_input

# print result
print("Removed suffix string:", trimmed_string)