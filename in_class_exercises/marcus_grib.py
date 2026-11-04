numbers = [1, 2, 3, 4, 5]
def reversing(x):
  lower_bound = 0
  upper_bound = len(numbers) - 1
  y = []
  while lower_bound < len(numbers) :

    y.append(x[upper_bound])
    upper_bound -= 1
    lower_bound += 1
  return y

newlist = reversing(numbers)

print(newlist)
