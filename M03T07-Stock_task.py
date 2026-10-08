##############################################################################
################################# M03T07 TASK ################################
##############################################################################


# Define class for stock list 

class Shoe:
    '''
    In this function, you must initialise the following attributes:
        ● country,
        ● code,
        ● product,
        ● cost, and
        ● quantity.
    '''
    # Constructor to assign attributes to class
    def __init__(self,country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Method returns cost of product
    def get_cost(self):
        return f"The {self.product} costs £{self.cost} "

    # Method returns quantity of product
    def get_quantity(self):
        return f"{self.quantity}"

    # String method returns strings of class objects
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

    # method returns strings of listed class objects
    # Source for referencing function can be found at: 
    # https://www.geeksforgeeks.org/python/sorting-objects-of-user-defined-class-in-python/
    def __repr__(self):
        return str((self.country, self.code, self.product, self.cost, self.quantity))
#=====================================Shoe list==============================#
'''
The list will be used to store a list of objects of shoes.
'''

shoe_list = []

# Define function to read inventory.txt
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    # Try statement prevents crashing if file doesn't exist
    try:
        # I/O operation used to open file
        with open("inventory.txt", "r") as file:
            # Source for skipping first line can be found at: 
            # https://www.w3schools.com/python/ref_func_next.asp
            next(file)     
            for lines in file:
        
                temp = lines.strip()
                temp = [item.strip() for item in temp.split(",")]
                shoe_list.append(Shoe(temp[0], temp[1], temp[2], float(temp[3]), int(temp[4])))

    # Displays error to user if file not found
    except FileNotFoundError as error:
        print("File is not in directory or doesn't exist")
        print("Place investory.txt file in ")
        print(error) 
        exit


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    print("Answer the prompts below to add to this list\n")

    # Check if shoe_list is populated yet

    if len(shoe_list) == 0:
        read_shoes_data()
    new_country = input("\nEnter country: ")
    new_code = input("\nEnter code: ")
    new_product = input("\nEnter product: ")
    new_cost = input("\nEnter cost: ")
    new_quantity = input("\nEnter quantity: ")
    
    shoe_list.append(Shoe(new_country, new_code, new_product, float(new_cost), int(new_quantity)))

    for shoe in shoe_list:
        print(shoe)


def view_all():
    # Check if shoe_list is populated yet

    if len(shoe_list) == 0:
        read_shoes_data()

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

    for shoe in shoe_list:
        print(shoe)

def re_stock():
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    if len(shoe_list) == 0:
        read_shoes_data()

    # Order shoes by quantity
    #for shoe in sorted(shoe_list, key = lambda shoe: shoe.quantity):
    sorted_shoes = sorted(shoe_list, key=lambda shoe: shoe.quantity)
    lowest_quantity_shoe = sorted_shoes[0]
    print("The quantity of the lowest in stock is: ", lowest_quantity_shoe)

    # Try statement to prevent crashing if user choice invalid
    try:
        user_choice = input("Restock item? (Y/N): ")

        # Validates user stamanet, accounting for case differences
        if user_choice.lower() == "y":
            new_quantity = int(input("Enter new quantity here: "))
            #Stores first list element with lowest quantity value
            sorted_shoes[0].quantity = new_quantity
            print("The quantity has been updated to: ", sorted_shoes[0])
        else:
            print("Items will not be restocked")
    except ValueError as error:
        print("Invalid input")
        print(error)

    # Write new shoe list to file
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

    

def search_shoe(input):
    if len(shoe_list) == 0:
        read_shoes_data()
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    # Iterate over the list. If we find the target item, return its index.
    # Example from course material PDF  
    for item in shoe_list: 
        if str(item.code) == input:
            return item
    # If the target item is not found, return None. 
        
    return None

def value_per_item():
    # Check if shoe list is populated yet
    if len(shoe_list) == 0:
        read_shoes_data()
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    
    # Iterate through list and return calculation
    for item in shoe_list:
        print("The total value of", str(item), " is: ", float(item.cost * item.quantity))

def highest_qty():
    
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    if len(shoe_list) == 0:
        read_shoes_data()

    # Order shoes by quantity

    sorted_shoes = sorted(shoe_list, key=lambda shoe: shoe.quantity)
    highest_quantity_shoe = sorted_shoes[-1]
    print("The ", highest_quantity_shoe.product, "is on sale! from", highest_quantity_shoe.country)


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

# Initial welcome message
print("Welcome to the Shoe stock manager!")
message = """
You can do the following: 
1. View all shoes
2. Get shoe cost
3. Get shoe quantity
4. Input new shoe entries
5. Restock shoe quantities for low stock items
6. View the total stock value
7. Find the highest quanitity item that's for sale

"""

# While loop ensures user stays within program until they exit
while True:
    # Prints menu options
    print(message)

    # try except loop prevents program crashing upon invalid user input
    try:
        user_choice = int(input("Enter the number of the menu option you want (8 to exit): "))
    except ValueError as error:
        print("Input invalid")
        print(error)
        continue
    # Validates user input
    if user_choice not in range(9):
        print("Choice not a valid option, please repeat entry")
        continue

    # Condition to view list
    if user_choice == 1:
        view_all()
    # Condition to view cost
    elif user_choice == 2:
        code = input("Enter shoe code: ")
        shoe = search_shoe(code)

        if shoe:
            print(shoe.get_cost())
        else:
            print("Shoe not found")

    # Condition to view quantity
    elif user_choice == 3:

        code = input("Enter shoe code: ")
        shoe = search_shoe(code)

        if shoe:
            print("The stock quantity is: ",shoe.get_quantity())
        else:
            print("Shoe not found")

    # Condition to accept new user entry
    elif user_choice == 4:
        capture_shoes()

    # Condition to increase stock quantity
    elif user_choice == 5:
        re_stock()

    # Condition to view item values
    elif user_choice == 6:
        value_per_item()

    # Condition to view highest quantity sale items
    elif user_choice == 7:
        highest_qty()

    # Condition to exit loop
    elif user_choice == 8:
        break
        



#read_shoes_data()
#capture_shoes()
#re_stock()
#search_shoe("SKU20207")
#value_per_item()
#highest_qty()