# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# Ask the user to input a string
main_string = input("Enter the main string: ")

# Ask the user to input the ending substring
ending_substring = input("Enter the ending substring: ")

# Length of the ending substring
end_length = len(ending_substring)

# Taking the final segment of the main string that is the same length as the ending substring
if len(main_string) >= end_length:
    taken_end = main_string[-end_length:]
else:
    taken_end = ""

# Comparison of the final segment with the ending substring and print result
if taken_end == ending_substring:
    print("The string is ending with the given substring.")
else:
    print("The string is not ending with the given substring.")