string = "banana"
new_string = ""

def reverse(string):
    new_string = string[-1:len(string)*-1-1:-1]
    print(new_string)
    
reverse(string)
