# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# prompt user for the string input
string_input = input("Enter the string: ")
width = int(input("Enter the width: "))

# spaces needed for the letters to go to the right
input_spaces = max(0, width - len(string_input))
  
# defining the right justified string
right_justified_string = " " * input_spaces + string_input

# print result
print(f"The right justified strings is: '{right_justified_string}'")