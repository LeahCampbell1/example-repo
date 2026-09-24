# Request user input for swimming in minutes, store in variable
swimming_time = int(input("Enter time in minutes to complete swimming: "))
# Request user input for cycling in minutes, store in variable
cycling_time = int(input("Enter time in minutes to complete cycling: "))
#Request user input for running in minutes, store in variable
running_time = int(input("Enter time in minutes to complete running: "))
# output total time
total_time = swimming_time + cycling_time + running_time
print(f"Total time taken for triathlon: ", total_time, " minutes")

# Use if-elif-else structure to print conditional responses to running time
if total_time >= 111:
    print("Award: No award")
elif total_time <= 110 and total_time >= 106: 
    print("Award: Provincial scroll")
elif total_time >= 101 and total_time <= 105:
    print("Award: Provincial half colours")
else: 
    print("Award: Provincial colours")