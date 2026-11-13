#possible solution havent tested for all possible cases
def collinerity (x1, y1, x2, y2):
    k = (x1 + x2 + y1 - y2) / 2
    if (x1 == 0 or x2 == 0) or (y1 == 0 or y2 == 0):
        return True
    elif (k*x2) % x1 == 0 and (k*y2) % y1 == 0:
        return True
    else:
        return False
    pass
