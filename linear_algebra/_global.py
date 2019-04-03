ACCURACY = 1e-8

def is_zero(x):
    return abs(x) < ACCURACY

def is_equal(x ,y):
    return abs(x-y) < ACCURACY
