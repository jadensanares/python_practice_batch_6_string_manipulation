# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# prompt user for input of string and substring
string_input = input("Enter the string: ")
substring = input("Enter the subtring you want to find from the last position: ")

# start the index variable
index_of_substring = -1

# loop string but in reverse 
for i in range(len(string_input) - len(substring), -1, -1):
    if string_input[i:i + len(substring)] == substring:
        index_of_substring = i
        break

# print result
if index_of_substring != -1:
    print("The last occurence of the substring is at index:", index_of_substring)
else:
    print("There are no substring found")