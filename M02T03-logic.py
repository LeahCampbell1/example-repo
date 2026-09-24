# The following program contains logic errors. 
# The program will run to completion, but not as logically intended

print("Welcome to the dog years calculator, where you can find out your dogs age in dog years")

user_age = input("Enter your dog's age; ") # this should be cast as an integer

dog_years = user_age * 7 # the string is multiplied seven times instead of the integer

print(f"Your dog is {dog_years} years old") # Logical error, the dogs age isn't output, but the repeated string is



