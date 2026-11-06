numbers = ["1", "2", "3"]


def reversing(x):
    process_ender = 0
    character_sliced = -1
    if isinstance(numbers, str):
        x.split()
    new_variable = []
    while process_ender < len(numbers):

        new_variable.append(x[character_sliced])
        character_sliced -= 1
        process_ender += 1
    if isinstance(numbers, str):
        new_variable = "".join(new_variable)
    return new_variable

new_variable = reversing(numbers)

print(new_variable)
