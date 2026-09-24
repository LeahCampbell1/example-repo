# Request user inputs intgeger, store input in variable
integer1 = int(input("Enter an integer: "))

# Request user inputs a second integer, store the input in a variable
integer2 = int(input("Enter a second integer:"))

# Continues to request unique integer, if second integer is equal to the first
while integer1 == integer2:
    integer2 = int(input("Enter a second UNIQUE integer: "))

# Request third integer, store input in variable
integer3 = int(input("Enter a third integer: "))

# Continues to request unique integer, if third integer is in the first or second integer variables 
while integer3 in [integer1, integer2]:
    integer3 = int(input("Enter a third UNIQUE integer: "))
    # Continues to request a unique integer, if third integer is equal to the second

# Create list of integers
integer_list = [integer1, integer2, integer3]

# Print sum of all numbers in "integer_list"
print("The sum of the numbers is " + str(sum(integer_list)))

# Print the first number minus the second number of numbers in "integer_list"
print("The first number minus the second number is: " + str(integer_list[0]-integer_list[1]))

# Print the third number multiplied by the first number of the numbers in "integer_list"
print("The third number multiplied by the first number is: " + str(integer_list[2]*integer_list[0]))

# Print the sum of numbers divided by the third number of "integer_list"
print("The sum of numbers in integer_list divided by the third number is: " + str(sum(integer_list)/integer_list[2]))


