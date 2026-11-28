import string
import math
import random as r
import thuc_tran as TT
# man I wish I could use classes in this class.
# it would allow me greater controll and give others in my group the ability to extend off of it

# this is the starting point for the token dictionary
# it creates a dictionary with 26 keys each being a letter of the alphabet
# it then assigns a dictionary to each of those keys

saved_tokens = {letter: {} for letter in string.ascii_lowercase}
context = []

def get_tokens ():
    return saved_tokens

# This is the function that takes a text input and turns it into tokens
# each word is its own token and it stores the frequency and location as well as the previous
# and following words as its relationships.
# Additionaly it creates the starting weight values to be adjusted later through an algorithm
# to prevent crashing it handles errors gracefully by and allows the program to continue running in
# the event of an error.

# Every once in awhile there is a key bug with saving new keys to the dictionary.
# Not really certain on the cause as it shouldn't get to that code where it is 
# currently throwing the error if that key doesn't exist.
# Fixed? by changing if v not in saved_tokens[v]
# to if i not in saved_tokens[v]
def send_text(*args):
    try:
        the_text = args[0].lower()
        tokens = the_text.split()
        context.append(tokens)
        for value, i in enumerate(tokens):
            print(value)
            previous = tokens[value - 1] if value > 0 else None
            following = tokens[value + 1] if value + 1 < len(tokens) else None
            v = i[0]
            print(i[0])
            if i not in saved_tokens[v]:
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
            for value, x in enumerate(saved_tokens[v][i]['weights']):
                y = saved_tokens[v][i]['location'][0]
                if y == 0:
                    adj = saved_tokens[previous[0]][previous]['location'][0] if previous != None and previous in saved_tokens[previous[0]] else -0.5
                    opp = saved_tokens[following[0]][following]['location'][0] if following != None and following in saved_tokens[following[0]] else 0.5
                    saved_tokens[v][i]['weights'][value] = round(math.cos((adj / opp) * 0.75 * r.randint(1, 3)), 2)
                else:
                    saved_tokens[v][i]['weights'][value] = round(x / (r.randint(1, y+1) - 0.07), 2)
        print(saved_tokens)
            # saved token the key is the value of the char and the list
            # has weights from 0 to 1 with index 0 being the location
            # object, action, determiner, describer, value, amount
            # [location, ]
    except ValueError:
        pass

def release(networth, Released_Label):
    assets = networth.get_number("assets")
    debts = networth.get_number("debts")
    income = networth.get_number("yearly_income")
    fine = networth.get_number("fine")
    fees = networth.get_number("court_fees")
    restitution = networth.get_number("restitution")
    forfeiture = networth.get_number("forfeiture")
    years = networth.get_number("sentence_years")
    before = TT.net_worth_before(assets, debts)
    loss = TT.total_loss(fine, fees, restitution, forfeiture, income, years)
    after = TT.net_worth_after(before, loss)
    sum_of_weights = 0
    total = 0
    print(context)
    for i, value in enumerate(context[0]):
        v= value[0]
        for x in saved_tokens[v][value]['weights']:
            print(x)
            sum_of_weights += x
    total = math.cos(sum_of_weights) * (math.cos(abs(after)) + 1) + math.cos(abs(years))
    if total > 0:
        if len(context[0]) >= 14:
            Released_Label.config(text="You can release: " + context[0][4].capitalize())
        else:
            Released_Label.config(text="You can release them")
    else:
        if len(context[0]) >= 14:
            Released_Label.config(text="Recommend to keep: " + context[0][4].capitalize() + " in prison")
        else:
            Released_Label.config(text="Recommend to keep them in prison")
