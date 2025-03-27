# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# Ask the user to enter a string
user_input = input("Enter a string: ")

# String that is all uppercase "all_upper = True"
all_upper = True

# Loop for the characters in the string
for character in user_input:
    if "a" <= character <= "z":
        all_upper = False
        break

# Print result
if all_upper:
    print("All characters of the string are uppercase.")
else:
    print("Not all characters of the string are uppercased.")