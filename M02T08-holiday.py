# This program calculates the users holidays costs from 
# the city destination, nights stay and amount of days 
# hiring a car

# The following contains functions

# Create function for cities
# Formatting reference uses course example code "Area.py" 
def cities():
    print("Choose a city from the following: ")
    print("1. New York")
    print("2. Lagos")
    print("3. Manila")
    print("4. Kingston")
    print("5. Nairobi")
    print("Type q to exit")

# Defines function for hotel cost
# Formatting reference uses course example code "Area.py"
def hotel_cost(num_nights):
    """
    Calculates total cost of hotel stay

    Parameters: 
    Takes num_nights

    Returns: 
    Total cost of hotel stay

    """
    return num_nights * hotel_in_city[city_flight]


# Defines function for plane cost

def plane_cost(city_flight): 
    """
    Calculates the plane cost 

    Parameters: 
    Takes city_flight

    Returns: 
    Cost of flight 
    """
    # If else format returns flight cost as integer
    # Formatting reference uses course example code "Area.py"
    if city_flight == "New York":
        return int(1000)
    elif city_flight == "Lagos":
        return int(1200)
    elif city_flight == "Manila": 
        return int(1800)
    elif city_flight == "Kingston": 
        return int(1000)
    elif city_flight == "Nairobi": 
        return int(1621)

# Defines function for car rental
# # Formatting reference uses course example code "Area.py"        
def car_rental(rental_days): 
    """
    Calculates total cost of car rental for stay

    Parameters: 
    Takes rental days

    Returns: 
    Total cost of car rental
    """
    return rental_days * car_rent_in_city[city_flight]

# Defines function for holiday cost
# Formatting reference uses course example code "Area.py"
def holiday_cost(x,y,z): 
    """
    """
    total_hotel = int(hotel_cost(x))
    total_plane = int(plane_cost(y))
    total_car = int(car_rental(z))

    holiday_total = total_hotel + total_plane + total_car
    print("The total cost of the holiday is £" + str(holiday_total))

# Uses dictionary to map user input to city
dict_cities = {
    "1":"New York",
    "2":"Lagos",
    "3":"Manila",
    "4":"Kingston",
    "5":"Nairobi",
}

# Uses dictionary to map city hotel cost
hotel_in_city = {
    "New York": 700,
    "Lagos": 400,
    "Manila": 150,
    "Kingston": 210,
    "Nairobi": 620,
}

# Uses dictionary to map car rent cost
car_rent_in_city = {
    "New York": 70,
    "Lagos": 40,
    "Manila": 15,
    "Kingston": 21,
    "Nairobi": 62,
}

# Print welcome message to user
print("This program will calculate your total holiday" \
" cost including plane, hotel and car rental cost.")

# Defines city flight
# Formatting reference uses course example code "code_word.py"
city_flight = "None"

# While loop initiates program for user input
# Formatting reference uses course example code "Area.py"
while True: 
    # Call cities function to display city options to user
    cities()
    # Store user choice of city in variable 
    # city_flight = dict_cities[str(input("\nEnter the number of your chosen city: "))]
    choice = input("\nEnter the number of your chosen city: ")
    
    if choice.lower() == "q":
        break

    if choice not in dict_cities:
        print("Input not recognised, repeat entry")
        continue

    city_flight = dict_cities[choice]

    # Prints calculations to user, referencing flight cost
    print(f"\nStaying at {city_flight}, costs" \
          " £", plane_cost(city_flight), "to fly to.")

    # Store number of nights in variable 
    num_nights = int(input("Enter the number of night's you'll be staying: "))
    print(f"\nStaying {num_nights}, costs £", hotel_in_city[city_flight], \
          # Prints calculations to user, referencing hotel cost
          "per night and £", hotel_cost(num_nights), " for the trip.")

    # Store the number of days user will rent car 
    rental_days = int(input("Enter number of day's you'll rent a car: "))
    # Prints calculations to user, referencing rental cost
    print(f"\nDriving {rental_days} days, costs ", car_rent_in_city[city_flight], " per" \
          "day and £",car_rental(rental_days), " for the whole trip.")

    # Prints total cost for user
    holiday_cost(num_nights,city_flight,rental_days)

    

