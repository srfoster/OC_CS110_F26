# Reversed List
list1 = [1, 2, 3, 4, 5]
reversed_list1 = list(reversed(list1))

print(reversed_list1)

# Mr. Stephen's list 

s = "chees"

new_string = ""

i = 1
last_letter_of_s = s[len(s) - i]
new_string = new_string + last_letter_of_s

i = 2
last_letter_of_s = s[len(s) - i]
new_string = new_string + last_letter_of_s

i = 3
last_letter_of_s = s[len(s) - i]
new_string = new_string + last_letter_of_s

i = 4
last_letter_of_s = s[len(s) - i]
new_string = new_string + last_letter_of_s

i = 5
last_letter_of_s = s[len(s) - i]
new_string = new_string + last_letter_of_s


for i in range(1,len(s)+1):
  last_letter_of_s = s[len(s)0 - i]
  new_string = new_string + last_letter_of_s

print(new_string)

############

s = "new_string = l + new_string"

new_string = ""

for l in s:
  new_string = l + new_string

print(new_string)
