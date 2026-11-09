name = input("Applicant name: ")
credit_score = int(input("Credit score: "))
age = int(input("Age: "))
annual_income = int(input("Annual Income: "))

if annual_income <= 64,220:
  
# DICTIONARY: how much the "algorithm" subtracts for each neighborhood
neighborhood_penalty = {
    "Maple Heights": 0,
    "Riverside": 80
}

# FUNCTION: takes income and neighborhood (parameters), returns a score
def calculate_score(income, neighborhood):
    # VARIABLE: the score starts from income alone
    score = 500 + income / 200
    # Subtract the neighborhood's penalty from the score
    score = score - neighborhood_penalty[neighborhood]
    return score

# Try it out with the same income in both neighborhoods
print(calculate_score(60000, "Maple Heights"))
print(calculate_score(60000, "Riverside"))
