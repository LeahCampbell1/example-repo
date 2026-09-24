# Imports statistics module 
import statistics

# Request user input for 10 floats and store in list 

# Set counter for user input
i = 0

# Define user input list 
user_input_list = []

# While loop to initiate user input on condition counter is
#  less than our equal to 10

while i < 10: 
    user_input = float(input("Enter a float here: "))
    user_input_list.append(user_input)
    i += 1

print(f"The sum of the number is the list is {sum(user_input_list)}")

# Define empty dictionary for list indexes
list_dict = {}

# Populate dictionary with indexes and corresponding values
for i in range(len(user_input_list)):
    list_dict[(user_input_list[i])] = [i]


# Get key for value which corresponds to max of the list
max_index = list_dict[max(user_input_list)]

# Print the max_index value, stripped of square brackets
print(f"The index of the largest float is {((str(max_index)).strip("]")).strip("[]")}")

# Get key for value which corresponds to min of the list
min_index = list_dict[min(user_input_list)]

# Print the min_index value, stripped of square brackets
print(f"The index of the smallest float is {((str(min_index)).strip("]")).strip("[]")}")

# Define mean of list
# Syntax reference used is: 
# https://docs.python.org/3/library/statistics.html#statistics.mean
mean_of_list = round(statistics.mean(user_input_list),2)

# Print mean of list in statement
print(f"The mean value of the list is {mean_of_list}")

# Define median of list
# Syntax reference used is: 
# https://docs.python.org/3/library/statistics.html#statistics.mean
median_of_list = round(statistics.median(user_input_list),2)

# Print median of list in statement
print(f"The median value of the list is {median_of_list}")


