# umbrella = "Leave me at home" 
# rain = False
# if rain: 
#    umbrella = "Bring me with"
# print(umbrella)

'''
current_time = 11 
if current_time <= 11: 
    print("Time for a short jog - let's go!") 

else: 
    print("It's after 11 - it's lunch time.")
    '''

hour = int(input("What is the hour?: "))

validate_input = (len(hour) > 2)

while validate_input:
    hour = input("Enter the 24 hour clock value please, just the first two digits: ")

if hour < 18: 
    greeting = "Good day" 
elif hour < 20: 
    greeting = "Good evening" 
else: greeting = "Good night"

print(greeting)