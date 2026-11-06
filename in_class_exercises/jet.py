'''
list = [1, 2, 3 , 4]

nuList = list[::-1]

print(nuList)




other solution

new_list = []

new_list = list.reverse()

print(new_list)

'''

word = "thing"

n = ""

i = 0
for j in range(len(word)):
    
    i = i - 1
    k = word[i]
    n = n + k

print(n)    