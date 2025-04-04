# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# Prompt the user to input string
string_input = input("Enter the string: ")
width = int(input("Enter the width: "))

# calculation of the number of zeros 
zeros_added = max(0, width - len(string_input))

# defining the string with zeros filled
zero_added_string = "0" * zeros_added + string_input

# print result
print("String with zeros added:", zero_added_string)