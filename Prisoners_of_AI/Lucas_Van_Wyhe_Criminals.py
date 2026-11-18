
import random

names = ["Aaron", "Benson", "Cole", "Daeson", "Evan", "Grant", "Hayden", "Isaac", "Jax", "Kaden", "Lucas", "Matthias", "Nolan", "Oliver", "Parker", "Quinn", "Robert", "Sergio", "Tye", "Uriah", "Vance", "Wyatt", "Xedemore", "Yasmine", "Zebedy"]
crimes = ["arson", "assault", "battery", "burglary", "corruption", "copyright infringement", "disorderly conduct", "drug possession", "election fraud", "environmental crimes", "forgery", "fraud", "harassment", "hate crimes", "identity theft", "insurance fraud", "kidnapping", "money laundering", "murder", "resisting arrest", "robbery", "smuggling", "stalking", "theft", "trespassing"]


def get_random_name():
    return random.choice(names)

def get_random_crimes():
    return random.sample(crimes, 3)

random_names = get_random_name()
random_crimes = get_random_crimes()

the_criminal = []
the_criminal.append([random_names, random_crimes])
print("This person's name is", random_names, "and they are charged with", random_crimes[0] + ",", random_crimes[1], "and", random_crimes[2])
print(the_criminal)
