list = [6, 1, 3, 2, 5, 4, 7, 9, 8]
new_list = []

for i in range(len(list)):
  new_list.append(list[-1])
  i = list[-1]
  list.remove(i)

print(new_list)
