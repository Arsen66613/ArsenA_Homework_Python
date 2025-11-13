import math


def square(side):
    square_area = side * side
    return math.ceil(square_area)


print(square(5))
