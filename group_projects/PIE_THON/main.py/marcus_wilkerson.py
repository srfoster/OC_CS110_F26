last_name = input("Applicant name: ")
credit_score = int(input("Credit score: "))

last_names1 = ["Martinez", "Gutierres", "Salinas", "Guillermo", "Hernandez", "Garcia", "Rodriguez", "Lopez", "Gonzales"]
last_names2 = ["Smith", "Roberts", "Johnson", "Williams", "Jones", "Anderson", "Davis", "Miller", "Leonard", "Brown"]

while credit_score < 670:
  if last_name in last_names2:
    print("Approved")
  else:
    print("Denied")

while credit_score >= 670:
  if last_name in last_names1:
    print("Denied")
  else:
    print("Approved")

  
