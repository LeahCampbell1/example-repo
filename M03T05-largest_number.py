# Source for structure formatting can be found at: 
# https://www.w3schools.com/python/python_recursion.asp

# Define function to take integer list as input
def find_largest_number(integer_list):
    # Set base case
    if len(integer_list) == 1:
        return integer_list[0]
    # Slice list
    else:
        remaining_integers = find_largest_number(integer_list[1:])
        # Return integer greater than other list elements
        return integer_list[0] if integer_list[0] > remaining_integers else remaining_integers
# Create list for testing
integer_list = [56,6,7,9,3,78]
#print result
print(find_largest_number(integer_list))