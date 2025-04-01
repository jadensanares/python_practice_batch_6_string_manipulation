# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# prompt the user to input string
string_input = input("Enter the string: ")
substring = input("Enter the substring for the count: ")

# start a counter for the occurences
count = 0

# make the loop for the string in able to check if the substring match with it
for i in range(len(string_input) - len(substring) + 1):
    if string_input[i:i + len(substring)] == substring:
        count += 1

# print result
