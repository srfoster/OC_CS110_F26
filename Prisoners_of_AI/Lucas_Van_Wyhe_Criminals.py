# grab a random name and assign a few crimes against that name for user scoring/judgement.

import random

names = ["Aaron", "Benson", "Cole", "Daeson", "Evan", "Grant", "Hayden", "Isaac", "Jax", "Kaden", "Lucas", "Matthias", "Nolan", "Oliver", "Parker", "Quinn", "Robert", "Sergio", "Tye", "Uriah", "Vance", "Wyatt", "Xedemore", "Yasmine", "Zebedy"]
crimes = ["Arson", "Assault", "Battery", "Burglary", "Corruption", "Copyright infringement", "Disorderly Conduct", "Drug Possession", "Election Fraud", "Environmetal Crimes", "Forgery", "Fraud", "Harassment", "Hate Crimes", "Identity Theft", "Insurance Fraud", "Kidnapping", "Money Laundering", "Murder", "Resisting Arrest", "Robbery", "Smuggling", "Stalking", "Theft", "Trespassing"]

random_names = random.choice(names)
random_crimes = random.sample(crimes, 3)

print("This person's name is", random_names, "and they are charged with", ", ".join(random_crimes))

