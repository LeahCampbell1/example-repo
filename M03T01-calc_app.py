# The following program performs simple calculations and
#  stores past calculations for the user to extract

##############################################################################
###############################  FUNCTIONS  ##################################

# Function for addition 

# Uses mathematic operand dictionary found at: 
# https://www.mathnasium.com/math-terms for reference 
# to mathematical operands

def addition(num1,num2): 
    """
    Function performs addition

    Parameters:
    Takes two floats
    Result: 
    Returns sum
    """
    result = num1 + num2
    return result

# Function for subtraction 

# Uses mathematic operand dictionary found at: 
# https://www.mathnasium.com/math-terms for reference 
# to mathematical operands

def subtraction(minuend,subtrahend): 
    """
    Function performs subtraction

    Parameters:
    Takes two floats
    Result: 
    Returns difference
    """
    result = minuend - subtrahend
    return result

# Function for multiplication 
# Uses source for built in math modules found at: 
# https://docs.python.org/3/library/math.html 

def multiplication(num1,num2):
    """
    Function performs multiplication

    Parameters:
    Takes two floats
    Result: 
    Returns product
    """
    product = num1 * num2
    return product

# Function for division
# Uses course example "Area.py" for reference to function formatting

# Uses mathematic operand dictionary found at: 
# https://www.mathnasium.com/math-terms for reference 
# to mathematical operands

def division(dividend,divisor):
    """
    Function performs division

    Parameters:
    Takes two floats. the dividend and divisor
    Result: 
    Returns quotient
    """
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError as error:
        print("It's not possible to divide by zero")
        print(error)


def write_to_file(calculation_statement):
    with open('./equations.txt', 'a+') as file:
        file.write("\n" + calculation_statement + "\n")

def read_equations():
    with open('equations.txt', 'r') as file: 
        for line in file: 
            print(line)

##############################################################################
############################  START OF PROGRAM  ##############################

# Output welcome message to user

welcome_message = """
Welcome to the calculator. You can perform 
simple calculations such as addition, subtraction,
 multiplication and division.
"""

print(welcome_message)

while True: 
    user_choice = (input("Enter C to calculate, V to view past " \
    "calculations or Q to quit: ")).lower()
    print(user_choice)
    acceptable_inputs = ["c", "v", "q"]

    if user_choice not in acceptable_inputs:
        print("Input not recognised please try again")
        continue

    if user_choice == "c": 

    # Request user input for calculation 
        input_message = """
        Enter a calculation, this program will only take two values. 
        The following calculations are available: addition (+), subtraction (-), 
        multiplication (*) and division (/): . 
        """
        print(input_message)

        # Request user input for float
        ## Catch error if float not entered
        try: 
            num1 = float(input("Enter first value: "))
        except ValueError as error: 
            print(error)
            print("Entry invlaid, please try again")
            continue

        # Request user inputs calculation type
        operator = input("Enter operator: ")
        print(operator)

        # Define list of acceptable operators
        acceptable_operations = ["+", "-", "*", "/"]

        # Validate user input, rerun loop if input invalid
        if operator not in acceptable_operations: 
            print("Operator not recognised, please try again")
            continue

        # Request user input for float
        ## Catch error if float not entered
        try:
            num2 = float(input("Enter second value: "))
        except ValueError as error: 
            print(error)
            print("Entry invlaid, please try again")
            continue

        # Map functions of operators in dictionary
        operator_mapping = {
            "+":addition,
            "-":subtraction,
            "*":multiplication,
            "/":division
        }

        # Apply addition function if 
        if operator == "+":
            # Take input as float (casting input reference). 
            output = operator_mapping["+"](num1,num2)
            print(output)
            calculation_statement = print(num1," + ",num2," = ", output)

            try:
                write_to_file(calculation_statement)
            except PermissionError as error:
                print("Could not write to file")
                print(error)
    
        elif operator == "-":
            minuend = num1
            subtrahend = num2
            output = operator_mapping["-"](minuend,subtrahend)
            print(output)
            calculation_statement = print(num1," - ",num2," = ", output)

        elif operator == "*":
            output = operator_mapping["*"](num1,num2)
            print(output)
            calculation_statement = print(num1," * ",num2," = ", output)

        elif operator == "/":
            dividend = num1
            divisor = num2

            output = operator_mapping["/"](dividend,divisor)
            print(output)
            calculation_statement = print(dividend," / ",divisor," = ", output)
            write_to_file(calculation_statement)


    elif user_choice == "v": 

        # print equations.txt 
        print("The previous calculations are")
        try: 
            read_equations()
        except FileNotFoundError as error:
            print("File not found") 
            print(error)

    elif user_choice == "q":
        print("Exiting program")
        break





