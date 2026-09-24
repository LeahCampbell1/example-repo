###################################################### INTEREST RATE CALCULATOR ###############################################################

# The following program is an interest rate calculator
# The user is prompted to state if they would like to calculate the value of an investment or a bond
# The user is further given the choice to calculate simple or compound interest on the investment

###############################################################################################################################################

# The math module is imported for later calculations
import math 


#### This section stores and valdates user input for "investment" or "bond"#####################################################################

# A greeting message is prepared. 
# Formatting makes reference to multiline strings from course material: "10-006 The String and Numerical Data Types.pdf"
greeting_message = '''Investment - to calculate the amount of interest you'll earn on your investment. 
Bond - to calculate the amount you'll have to pay on a home loan. 
Enter either “investment” or “bond” from the menu above to proceed: '''

# The user is prompted to enter a choice between "investment" or "bond". 
# The input is stored in lower case to accept variations of capitalisation
user_choice = input(greeting_message).lower()

# Uses logical operator to check input is equal to “investment” or “bond”
## For  reference to list manipulation, course material "10-017_Data Structures – The List" is used. 
## For reference to while statement, previous answer for M01T01 "psuedo.txt" is used.
while user_choice not in ["investment","bond"]:
    # User is repeatedly prompted for a valid input whilst the logal operator remains True
    print("Input is not recognised, please try again")
    user_choice = input(greeting_message).lower()

#### This section outputs the interest range, depending on conditions met by the user input ######################################################

# The if statement checks the previous user input for interest type 
## For  reference to if-else structures, course material "10-010_Control Structures – If, Elif, Else and the Boolean Data Types" is used.
if user_choice == "investment":

    # User is prompted to input deposit, interest rate and repayment duration.
    # Inputs are stored as floats
    deposit = float(input("Enter the deposit amount: "))
    interest_rate = float(input("Enter the percentage interest rate: "))
    investment_years = float(input("Enter the number of years you intend to invest: "))

    # Accept input despite capitalisation
    interest = input("State 'simple' or 'compound' interest: ").lower()

    # Check input conforms to conditions before continuing
    ## For reference to while statement, previous answer for M01T01 "psuedo.txt" is used.
    while interest not in ["simple","compound"]:
        print("Input is not recognised, please try again")
        interest = input("State 'simple' or 'compound' interest: ").lower()

    # The condition if statement for condition when "simple" is selected
    if interest == "simple": 
        # Hold the equation for simple interest in a variable
        total_simple_interest = deposit * (1 + (interest_rate/100) * investment_years)
        # Outputs total investment value to console
        # Formatting of payment amount references "PEP 378: Format Specifier for Thousands Separator" 
        ## (at: https://docs.python.org/dev/whatsnew/2.7.html#pep-0378)
        formatted_simple_interest = '{:20,.2f}'.format(total_simple_interest)
        print(f"The total amount once interest is applied is:{formatted_simple_interest}")

    # else statement for condition when "compound" is selected
    elif interest == "compound":
        total_compund_interest = deposit * math.pow(1 + (interest_rate/100),investment_years)
        # Formatting of payment amount references "PEP 378: Format Specifier for Thousands Separator" 
        ## (at: https://docs.python.org/dev/whatsnew/2.7.html#pep-0378)
        formatted_compund_interest = '{:20,.2f}'.format(total_compund_interest)
        print(f"The total amount once interest is applied is: {formatted_compund_interest}")

# else statement for if bond is selected
else: 
    present_value_of_house = float(input("Enter the current value of the house: "))
    interest_rate = float(input("Enter your interest rate as a percentage: "))
    months_to_repay_bond = int(input("Enter the total months it will take to repay the bond: "))
    # Calculates monthly interest
    monthly_interest_rate = (interest_rate/100)/12
    # Applies formula for bond repayment
    repayment = (monthly_interest_rate*present_value_of_house)/ (
        1-math.pow(1+monthly_interest_rate, -months_to_repay_bond
                  ))
    # Formatting of payment amount references "PEP 378: Format Specifier for Thousands Separator"
    ## (at: https://docs.python.org/dev/whatsnew/2.7.html#pep-0378)
    formatted_repayment = '{:20,.2f}'.format(repayment)
    print(f"The total repayment will be: {formatted_repayment}")



