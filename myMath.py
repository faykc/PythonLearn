from functools import reduce

def addition(*x):
    return reduce(lambda y,r: y+r, x)

