# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# Prompt the user for the input
string_input = input("Enter a string with trailing spaces: ")

# remove trailing spaces without using rstrip() function
last_char_index = len(string_input) -  1
while last_char_index >= 0 and string_input[last_char_index] == " ":
    last_char_index -= 1

# Trimming the string 
trimmed_string = string_input[:last_char_index + 1]

# print result
print(f"Trimmed string: '{trimmed_string}'")