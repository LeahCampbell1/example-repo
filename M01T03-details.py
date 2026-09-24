# Request user input, store string in "name variable"
Name = input("Enter your name: ")

# Request user input, store integer in "Age" variable
Age = int(input("Enter your age: "))
new_age = Age + 1

# Request user input, store string in "House Number" variable
House_number = input("Enter your house number: ")

# Request user input, store string in "Street name" variable
Street_name = input("Enter your street name: ")

# Prints greeting message to check birthday party address
print(f"Very nice to meet you {Name}, you barely look {Age} years old. Just want to make sure when you turn {new_age} on your next birthday that I come to the right address: {House_number} of {Street_name} street")