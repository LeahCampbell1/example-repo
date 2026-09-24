# Defines function to take arguments, integer list and index
# Source for structure formatting can be found at: 
# https://www.w3schools.com/python/python_recursion.asp
def sum_recursion(integer_list,index):

    # Structure if-else condition to check when list length is equal to integer
    if len(integer_list) == index:
        # 0 will not allow more calculations
        return 0
   # Otherwise call the function and reduce index by one
    else:
        return integer_list[index] + integer_list[index-1]

# prints function call for testing
print(sum_recursion(range(10),7))
