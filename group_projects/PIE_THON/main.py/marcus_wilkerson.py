last_name = input("Applicant name: ")
credit_score = int(input("Credit score: "))

last_names1 = ["Martinez", "Gutierres", "Salinas", "Guillermo", "Hernandez", "Garcia", "Rodriguez", "Lopez", "Gonzales"]
last_names2 = ["Smith", "Roberts", "Johnson", "Williams", "Jones", "Anderson", "Davis", "Miller", "Leonard", "Brown"]

def check_credit_score():  
  while credit_score < 670:
    if last_name in last_names2:
      return "Approved"
    else:
      return "Denied"
  while credit_score >= 670:
    if last_name in last_names1:
      return "Denied"
    else:
      return "Approved"

print(check_credit_score())

  
