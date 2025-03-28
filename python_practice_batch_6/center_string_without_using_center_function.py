# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# Get user input for the string
text_string = input("Enter the string: ")
total_width = int(input("Enter the total width: "))
  
# Computation of spaces.
left_spaces = (total_width - len(text_string)) // 2
right_spaces = total_width - len(text_string) - left_spaces

# print result
print(f"'{ ' ' * left_spaces + text_string + ' ' * right_spaces }'")
