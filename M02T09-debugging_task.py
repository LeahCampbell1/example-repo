# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):

    # Unhash below print statement to verify list is cast correctly
    #print(list(keys))
    for key in list(keys):
        # Runtime error: k should be changed to "key"
        print(dictionary[key])

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         # Syntax error: 'd'oh' should be in double quotes
                         "homer": "d'oh!", 
                         "maggie": "(Pacifier Suck)"
                         }

# Syntax error, second argument should be enclosed in parenthesis

print_values_of(simpson_catch_phrases,('lisa', 'bart', 'homer'))

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

