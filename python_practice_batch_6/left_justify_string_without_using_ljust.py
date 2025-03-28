# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# Ask the user to enter the input (string)
text_string = input("Enter the string: ")

# Ask the user to enter the width for spaces
total_width = int(input("Enter the total width: "))

# condition for adding of spaces
spaced_string = text_string + " " * max(0, total_width - len(text_string))

# print result
print(f"Spaced string: '{spaced_string}'")