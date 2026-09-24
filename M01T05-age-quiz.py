# Print introductory statement to the user
print("Welcome to the age quiz!")
# Prompt user to enter age and store in variable
age = int(input("Enter your age: "))
# Use if-elif-else structure to respond to age with the required response
if age >= 100:
    print("Sorry you're dead")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill")
elif age == 21:
    print("Congrats on your 21st!")
elif age <= 13:
    print("You qualify for the kiddie discount.")
# End statement with response for unspecified conditions 
else: 
    print("Age is but a number")