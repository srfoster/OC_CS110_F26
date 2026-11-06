lists = [1,2,3,4,5,6]
lists.sort(reverse = True)
print(lists)

#Riverse a string
Words = "Hello world"
for X in Words[-1:-12:-1]:
    print(X.strip())


s = "apple"
new_string = ""
for Y in range (1,len(s)+1):
#step 1b
    last_letter_of_s = s[len(s) -Y]
#step 1c
    new_string = new_string + last_letter_of_s

print(new_string)

#if
s = "Hello world"
new_string = ""
for Y in range (1,len(s)+1):
#step 1b
    last_letter_of_s = s[len(s) -Y]
#step 1c
    new_string = last_letter_of_s + new_string
    print(new_string)
#It would be "Hello world" because of strings ex. "d" + "" -> "l" + "d" -> "r" + "ld" ->....->"Hello world"

#-----Note----------
#In: "apple"
#Out:"elppa"
s = "apple"
#Step1. (a)Take last; (c)put at start of (b)new string ->"e"
#step 1a
new_string = ""
#step 1b
last_letter_of_s = s[len(s)-1]
#step 1c
new_string = new_string + last_letter_of_s

print(new_string)

#step 2a
new_string = ""
#step 2b
last_letter_of_s = s[len(s)-2]
#step 2c
new_string = new_string + last_letter_of_s

print(new_string)
