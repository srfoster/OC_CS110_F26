# grab a random name and assign three crimes against that name for user scoring/judgement.

import random

names = ["Aaron", "Benson", "Cole", "Daeson", "Evan", "Grant", "Hayden", "Isaac", "Jax", "Kaden", "Lucas", "Matthias", "Nolan", "Oliver", "Parker", "Quinn", "Robert", "Sergio", "Tye", "Uriah", "Vance", "Wyatt", "Xedemore", "Yasmine", "Zebedy"]
crimes = ["arson", "assault", "battery", "burglary", "corruption", "copyright infringement", "disorderly conduct", "drug possession", "election fraud", "environmental crimes", "forgery", "fraud", "harassment", "hate crimes", "identity theft", "insurance fraud", "kidnapping", "money laundering", "murder", "resisting arrest", "robbery", "smuggling", "stalking", "theft", "trespassing"]

random_names = random.choice(names)
random_crimes = random.sample(crimes, 3)

print("This person's name is", random_names, "and they are charged with", random_crimes[0] + ",", random_crimes[1], "and", random_crimes[2])
