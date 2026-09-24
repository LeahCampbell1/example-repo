# Request input from user
user_input = input("Enter your name: ")

# create empty list for incorrect strings
incorrect_strings = []

# While loop with condition user_input is not equal
# to John

while user_input.lower() != "john":
    incorrect_strings.append(user_input)
    # While loop continually asks for name
    user_input = input("Enter your name: ")

# Print list of incorrect names
print(f"Incorrect names: {incorrect_strings}")