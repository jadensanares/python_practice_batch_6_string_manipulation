# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# prompt user for string input
string_input = input("Enter the string: ")
prefix = input("Enter the prefix: ")

# check the string if it starts with the given prefix by the user
is_prefix = string_input[:len(prefix)] == prefix

# print result
if is_prefix:
    print("The string starts with the prefix:", prefix)
else:
    print("The string does not start with", prefix)