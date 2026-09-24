################## LIST TYPES TASK ####################### 

# Stores the names of three friends in a list calles friends_names
friends_names = ['Yasmin', 'Harold', 'Kurt']

# Prints name of first friend
print(friends_names[0])

# Prints name of last friend
print(friends_names[-1])

# Defines new list of friends ages, called 'friends_ages'
friends_ages = [30,34,29]

# Create a list of indexes using the range function called place_in_list
# This lists indexes, using the len function to return the list length
# Used course material "10-017_Data Structures – The List" for reference to range function
place_in_list = list(range(0,len(friends_names)))
print(place_in_list)

# The for loop iterates through the "place_in_list", 
#   calling the corresponding list element from the lists of names and ages. 
# Using list items to call
# Used course material "10-017_Data Structures – The List" for reference to
for place in place_in_list:
    print(f"{friends_names[place]} is {friends_ages[place]} years old")


