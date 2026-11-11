import string

# man I wish I could use classes in this class.
# it would allow me greater controll and give others in my group the ability to extend off of it

# this is the starting point for the token dictionary
# it creates a dictionary with 26 keys each being a letter of the alphabet
# it then assigns a dictionary to each of those keys

saved_tokens = {letter: {} for letter in string.ascii_lowercase}

# This is the function that takes a text input and turns it into tokens
# each word is its own token and it stores the frequency and location as well as the previous
# and following words as its relationships.
# Additionaly it creates the starting weight values to be adjusted later through an algorithm
# to prevent crashing it handles errors gracefully by and allows the program to continue running in
# the event of an error.

def send_text(*args):
    try:
        the_text = the_input.get()
        tokens = the_text.split()
        for value, i in enumerate(tokens):
            print(value)
            previous = tokens[value - 1] if value > 0 else None
            following = tokens[value + 1] if value + 1 < len(tokens) else None
            v = i[0]
            print(i[0])
            if v not in saved_tokens[v]:
                saved_tokens[i[0]][i] = {
                    'frequency': 0,
                    'weights': [1,1,1,1,1,1],
                    'relationships': {-1: previous, 1: following},
                    'location': [value]
                }
            else:
                saved_tokens[i[0]][i]['frequency'] += 1
                saved_tokens[i[0]][i]['location'].append(value)
                saved_tokens[i[0]][i]['relationships'][-1] = previous
                saved_tokens[i[0]][i]['relationships'][1] = following
        print(saved_tokens)
            # saved token the key is the value of the char and the list
            # has weights from 0 to 1 with index 0 being the location
            # object, action, determiner, describer, value, amount
            # [location, ]
    except ValueError:
        pass
