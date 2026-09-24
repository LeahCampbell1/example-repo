
##############################################################################
################################# TASK 1 #####################################
##############################################################################
## List is not in order so the linear search will be used

# Define function for linear search
def linear_search(target, sample_list): 
    # Iterate over the list to find index of target 
    for index in range(len(sample_list)): 
        if sample_list[index] == target: 
            return index 
    # Return None if target not in list 
    return None 

##############################################################################
################################# TASK 2 #####################################
##############################################################################

# Input list and 
sample_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target = 9
print("Target found at index: ",linear_search(target,sample_list) )

# Insertion sort source used to complete task can be found at: 
# https://www.w3schools.com/python/python_dsa_insertionsort.asp

##############################################################################
################################# TASK 3 #####################################
##############################################################################

def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        insert_index = i
        value = array.pop(i)
        for j in range(i-1,-1, -1): 
            if array[j] > value:
                insert_index = j
        array.insert(insert_index, value)
    print(array)

print(insertion_sort(sample_list))


##############################################################################
################################# TASK 3 #####################################
##############################################################################

# Binary search will now be used on the list as it is sorted. Previously it 
# wasn't. 
# 
# Real world applications of this search type would be identifying a
# products position in an inventory, for example a clinical sample in a 
# laboratory fridge in a LIMS system

def binary_search(target, list):
    low, high = 0, len(list) -1

    while high >= low: 
        middle = (low + high)// 2
        if list[middle] == target:
            return middle
        elif list[middle] < target:
            low = middle +1 
        else: 
            high = middle -1
    return None

print(binary_search(16,sample_list))