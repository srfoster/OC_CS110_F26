numbers = "12345678"


def reversing(x):
    lower_bound = 0
    upper_bound = len(numbers) - 1
    new_string = ""
    while lower_bound < len(numbers):

        new_string += x[upper_bound]
        upper_bound -= 1
        lower_bound += 1
    return new_string

new_string = reversing(numbers)

print(new_string)

