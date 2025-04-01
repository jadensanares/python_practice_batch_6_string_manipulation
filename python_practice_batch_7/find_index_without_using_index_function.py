# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# prompt user for the input string and substring
string_input = input("Enter the string: ")
substring = input("Enter the substring you want to find in the string: ")

# start the index variable
index_of_substring = -1

# start the loop for finding the first occurence of said substring
for i in range(len(string_input) - len(substring) + 1):
    if string_input[i:i + len(substring)] == substring:
        index_of_substring = i
        break     # to stop the loop if occurence is found

# print result
if index_of_substring != -1:
    print("The substring is at index:", index_of_substring)
else:
    print("There is no substring found")