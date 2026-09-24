# Request input from user
str_manip = input("Enter sentence here: ")

# Print length of sentence to console
print(len(str_manip))

# Store the last letter of the string in a variable
last_letter = str_manip[-1]

# Replace with "@" any character in the sentence which matches the last letter of the users sentence
print(str_manip.replace(last_letter,"@"))

# Print the last three characters backwards
# Used course material "10-006 The String and Numerical Data Types.pdf" page 7 to complete the function
print(str_manip[-1:-4:-1])

# Store first three characters in variable
first_3_characters = (str_manip[:3])

# Store last two characters in variable
last_two_characters = (str_manip[-2:])

# Print the output produced, by joining the two variables which store the first three, and last two characters
print(first_3_characters+last_two_characters)

