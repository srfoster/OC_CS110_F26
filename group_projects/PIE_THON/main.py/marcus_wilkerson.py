print(


last_name = input("Applicant name: ")
credit_score = int(input("Credit score: "))

last_names1 = ["Martinez", "Gutierres", "Salinas", "Guillermo", "Hernandez", "Garcia", "Rodriguez", "Lopez", "Gonzales", "Sanchez", "Ramirez", "Rivera", "Gomez"
              "Reyes", "Cruz", "Diaz"]
last_names2 = ["Smith", "Roberts", "Johnson", "Williams", "Jones", "Anderson", "Davis", "Miller", "Leonard", "Brown", "Thomas", "Taylor", "Clark", "Lewis" 
              "Foster", "Long", "Myers"]

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

  
def run_module(): # main module loop
    
    # prints initial header
    print()
    print("=== Loan Approval Survey ===")
    print("Please answer each question truthfully.")
    print("You will recieve points based on your responses.")    
    print("You need at least", APPROVAL_CUTOFF, "points to be approved.")

