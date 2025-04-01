# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# prompt user to input string
string_input = input("Enter the string: ")

# checking if all characters of the string is on lower case
all_char_lowercase = True

for character in string_input:
    if "A" <= character <= "Z":
        all_char_lowercase = False

# print the result
if all_char_lowercase:
    print("All characters in the string are in lowercase.")
else:
    print("Not all characters in the string are in lowercase.")