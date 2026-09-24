# Import random module 

import random

list_of_jokes = [
    ["Why didn't the skeleton go to the dance?", "It had nobody to go with"],
    ["Why are pirates pirates?", "Because they aaaaaar"],
    ["Why are there no pills in the jungle?", "Because the paracetamol"],
    ["What was the hedgehog dong in the sky", "Falling"],
    ["What happened when the grape got trodden on", "It let out a little wine"],
]

# Check if there's still jokes in the list 
# Used course example program "list_application.py" for reference
if len(list_of_jokes) == 0:
    print("No questions were given.")


# Set iteration count to 0
user_choice = input("Want to hear a joke? (y/n): ")

# Request user input
while user_choice.lower() == "y":
    # Insert randon integer within range of the joke list length -1 to 
    # avoid being out of range
    # As indicated by source used for reference: 
    # https://docs.python.org/3/library/random.html#module-random
    # The second argument is synonymous to int + 1
    joke = list_of_jokes[random.randint(0,(len(list_of_jokes)-1))]
    print(f"{joke[0]} \n {joke[1]}")
    user_choice = input("Want to hear a joke? (y/n): ")
