###################################################### INTEREST RATE CALCULATOR ###############################################################

# The following program is an interest rate calculator
# The user is prompted to state if they would like to calculate the value of an investment or a bond
# The user is further given the choice to calculate simple or compound interest on the investment

###############################################################################################################################################

# The math module is imported for later calculations
import math 


#### This section stores and valdates user input for "investment" or "bond"#####################################################################

# A greeting message is prepared, formatting makes reference to multiline strings from course material "10-006 The String and Numerical Data Types.pdf"
greeting_message = '''Investment - to calculate the amount of interest you'll earn on your investment. 
Bond - to calculate the amount you'll have to pay on a home loan. 
Enter either “investment” or “bond” from the menu above to proceed: '''

# The user is prompted to enter a choice between "investment" or "bond". 
# The input is stored in lower case to accept variations of capitalisation
user_choice = input(greeting_message).lower()

# Uses logical operator to check input is equal to “investment” or “bond”
while user_choice not in ("investment", "bond"):
    # User is repeatedly prompted for a valid input whilst the logal operator remains True
    print("Input is not recognised, please try again")
    user_choice = input(greeting_message).lower()

#### This section outputs the interest range, depending on conditions met by the user input ######################################################

# The if statement checks the previous user input for interest type 
if user_choice == str("investment"):
    # User is prompted to input deposit, rate and repayment duration, inputs are stored in variables
    deposit = float(input("Enter your deposit amount: "))
    interest_rate = float(input("Enter your interest rate as a percentage: "))
    investment_years = int(input("Enter the number of years you intend to invest: "))
    # Accept input despite capitalisation
    interest = input("State if you want 'simple' or 'compund' interest: ").lower()


    # Check input conforms to conditions before continuing
    while interest not in ("simple", "compound"):
        print("Input is not recognised, please try again")
        interest = input("State if you want 'simple' or 'compund' interest: ").lower()


    # if statement for condition when "simple" is selected
    if interest == str("simple"): 
        # Hold the equation for simple interest in a variable
        total_simple_interest = deposit * (1 + (interest_rate / 100) * investment_years)
        # Outputs total investment value to console
        print(f"Your total amount once interest is applied is: {total_simple_interest}")

    # else statement for condition when "compound" is selected
    elif interest == str("compound"):
        total_compund_interest = deposit * math.pow(1 + (interest_rate / 100),investment_years)
        print(f"Your total amount once interest is applied is: {total_compund_interest}")
    else: 
        print("Invalid input")
elif user_choice == str("bond"): 
    present_value_of_house = int(input("Enter the current value of the house: "))
    interest_rate = float(input("Enter your interest rate as a percentage: "))
    months_to_repay_bond = int(input("Enter the total months it will take to repay the bond: "))
    month_rate = (interest_rate / 100) / 12
    repayment = (month_rate * present_value_of_house) / ( 1- math.pow(1 + month_rate, -months_to_repay_bond ))
    print(f"The total repayment will be {repayment}")
else: 
    print("Invalid input")



