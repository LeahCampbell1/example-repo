# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Error type: Runtime error. Variable should be cast as a string
animal_type = "cub"
number_of_teeth = int(16) # Error type: Runtime error. Variable should be cast as an integer


# Error type: Syntax error variables need to be called with f-string
# Error type: Logical error. The variables for "number of teeth" and "animal type" need to be switched. 
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" 


print(full_spec) # Error type: Syntax error and Runtime error. Print statement needs parenthesis. Variable formatting f-string

