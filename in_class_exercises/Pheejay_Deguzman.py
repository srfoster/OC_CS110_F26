

s ="chicken nuggets"

new_string = ""

for i in range(1,len(s)+1):
    last_letter_of_s = s[len(s) - i]
    new_string = new_string + last_letter_of_s
    
print(new_string)
