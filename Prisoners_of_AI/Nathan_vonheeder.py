#starting point of my module, going to be about if a prisoner can get a job based on their conviction


prisoner_job_scores = [
  [50, 50, 50],
  [60, 60, 60],
  [70, 70, 70],
]
#just trying to get an idea down and a starting point might change it from a loop later on
for job in prisoner_job_scores:
  total = 0
  for sub_score in job:
    total += sub_score

  if total < 170:
    print(total, "denied")
  elif total <= 200:
    print(total, "needs interview")
  else:
    print(total, "approved")

