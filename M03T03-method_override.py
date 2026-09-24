# Creates Adult class

class Adult:
    # Constructor method with instance variables name, age, eye colour and hair colour
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    # Method for user can drive
    def can_drive(self):
        print(self.name," is old enough to drive")

# Creates subclass Child
class Child(Adult):
    # Contructor method with Adult instance variables
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)

    # Method for user can't drive
    def can_drive(self):
        print(self.name," is not old enough to drive")


# Prompts user for input
name = input("Enter your name here: ")
age = int(input("Enter your age here: "))
hair_colour = input("Enter your hair colour here: ")
eye_colour = input("Enter your eye colour here: ")

# Logic to output condition if user is over 18
if age >= 18:
    user = Adult(name, age, eye_colour, hair_colour)

# Logic to output condition if user is under 18
elif age < 18:
    user = Child(name, age, eye_colour, hair_colour)

# Apply method to output
user.can_drive()
