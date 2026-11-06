numbers = "123"


def reversing(x):
    character_sliced = -1
    new_variable = []
    for i in range(len(numbers)):

        new_variable.append(x[character_sliced])
        character_sliced -= 1
    if isinstance(numbers, str):
        new_variable = "".join(new_variable)
    return new_variable

new_variable = reversing(numbers)

print(new_variable)

