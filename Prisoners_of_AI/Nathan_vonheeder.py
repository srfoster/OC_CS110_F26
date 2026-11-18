#starting point of my module, going to be about if a prisoner can get a job based on their convictio
#CHECK SPELLING YOU FIVE FINGERED NUTJOB

prisoner_job_scores = [
  [50, 50, 50],
  [60, 60, 60],
  [70, 70, 70],
]

prisoners = {
  1: "john",
  2: "david",
  3: "daniel",
  4: "luke",
  5: "mark",
  6: "dewayne",
  7: "peter",
}
for job in prisoner_job_scores:
  total = 0
  for sub_score in job:
    total += sub_score
 #work on making it not repeat a name  
  import random
  number = random.randint(1, 7)
  name = prisoners[number]

  if total < 170:
    print(name, total, "denied")
  elif total <= 200:
    print(name, total, "needs interview")
  else:
    print(name, total, "approved")
    

