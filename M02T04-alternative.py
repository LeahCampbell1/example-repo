# The following prgram is the string manipulation task of 10-016 "String manipulation"

# Store user input in variable 
user_input_string = input("Enter the lyrics to your faviroute song: ")
manipulated_string = ""

# Loop through each integer, stored in the range of the string length. 
# Hyperion course material youtube video "String Handling" was referenced for 
# consructing for loop at: 
# https://youtu.be/qK5tXwUdK1U?si=gRYR54xeQR2SZcg4
for i in range(len(user_input_string)): 

    # For each iteration that returns 1 when tested with modulo 2
    # Turn the iterable to upper and store in string 
    if i % 2 == 0: 
        manipulated_string += user_input_string[i].upper()

    # If modulo 2 of the interation doesn't equal 1, 
    # turn the case to lower
    else: 
        manipulated_string += user_input_string[i].lower()

# Print the new string to the console
print(manipulated_string)

# Split string and store in list 
split_user_input = user_input_string.split(" ")

# Create empty list to store words from list manipulation
manipulated_list = []

# Loop through list and apply same manipulation as before
# Use the range of the length of the list
for i in range(len(split_user_input)):
    # Create condition for the even iterations
    if i % 2 == 0: 
        # Add the lower case manipulated string to the new list
        # Add a space to the new list item to keep words formatted
        manipulated_list += (split_user_input[i].lower() + " ")
    else: 
        # Add the upper case manipulated string to the new list
        # Add a space to the new list item to keep words formatted
        manipulated_list += (split_user_input[i].upper() + " ")

# print the joined list
print("".join(manipulated_list))

