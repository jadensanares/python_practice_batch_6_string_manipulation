# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# prompt user input (string)
input_string = input("Enter the string: ")

# splitting of words
words = input_string.split()

# checking conditions of the word
added_words = []
for word in words:
    if word:
        added_word = word[0].upper() + word[1:].lower()
    else:
        added_word = ""

    added_words.append(added_word)

titled_string = " ".join(added_words)

# print result
print("Titled string:", titled_string)