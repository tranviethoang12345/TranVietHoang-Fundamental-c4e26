
def is_inside(x, y):
    if x[0] < y[0] or x[0] > y[0] + y[2]:
        return False
    else:
        if x[1] < y[1] or x[1] > y[1] + y[3]:
            return False
        else:
            return True

