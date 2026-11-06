s = "apple"

#Step 1a
new_string = ""

#Step 1b
last_letter_of_s = s[len(s) -1] #len works for most languages

#Step 1c
new_string = new_string + last_letter_of_s

#Step 2a
last_letter_of_s = s[len(s) -2] 

#Step 2b
new_string = new_string + last_letter_of_s

#Step 3a
last_letter_of_s = s[len(s) -3]

#Step 3b
new_string = new_string + last_letter_of_s

#Step 4a
last_letter_of_s = s[len(s) -4]

#Step 4b
new_string = new_string + last_letter_of_s

#Step 5a
last_letter_of_s = s[len(s) -5]

#Step 5b
new_string = new_string + last_letter_of_s

#print(new_string)

for i in range(1, len(s)+1):
  last_letter_of_s = s[len(s) - i]
  new_string = new_string + last_letter_of_s

#print(new_string)

for l in s:
  new_string = 1 + new_string

print(new_string)
