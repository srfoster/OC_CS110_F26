numbers = "12345678"


def reversing(x):
    process_ender = 0
    character_sliced = -1
    new_string = ""
    while process_ender < len(numbers):

        new_string += x[character_sliced]
        character_sliced -= 1
        process_ender += 1
    return new_string

new_string = reversing(numbers)

print(new_string)


