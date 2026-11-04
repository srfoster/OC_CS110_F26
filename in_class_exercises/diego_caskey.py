word = "apple"
length = len(word)
reversed = ""
for i in range(length):
    index = length - 1 - i
    reversed_word += word[index]
print(reversed_word)
