# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


# Syntax error: Statement requires parenthesis
print("Welcome to the error program") 

# Syntax error: Statement requires parenthesis
# Runtime error: Unnecessary indent 
print("\n") 

# Variables declaring the user's age, casting the str to an int, and printing 
# the result
# Runtime error: Defining a variable uses a single "="
age_Str = "24 years old" 

# Runtime error: string can't be cast as integer. 
# Integer must be selected from string using indexes
age = int(age_Str[0:2]) 

# Runtime error: Integer must be cast as string to be printed
# Logical error, statement should have spaces
print("I'm " + str(age) + " years old.") 


# Variables declaring additional years and printing the total years of age

# Logical error: string should be cast as integer
years_from_now = "3" 

# Logical error: string should be cast as integer
total_years = age + int(years_from_now) 

# Syntax error: statement requires parenthesis
# Logical error: variables should be formatted with f-string and "answer_years"
# was not a defined variable
print(f"The total number of years: {str(total_years)}") 
                                                      

# Variable to calculate the total number of months from the given number of 
# years and printing the result

# Runtime error: "total" isn't defined as a variable
total_months = total_years * 12 

# Syntax error: Statament requires parethesis and f-string is needed to call
#  variable (cast as string). 
# Logical error: 6 months needed to be added to the calculation
print(f"In 3 years and 6 months, I'll be {str(total_months + 6)} months old") 

#HINT, 330 months is the correct answer

