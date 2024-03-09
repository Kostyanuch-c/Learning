from math import gcd


def make(numer, denom):
    nod = gcd(numer, denom)
    return f'{int(numer / nod)}/{int(denom / nod)}'


def get_numer(rat):
    return int(rat.split('/')[0])


def get_denom(rat):
    return int(rat.split('/')[1])


def add(rat1, rat2):
    x1, y1 = get_numer(rat1), get_denom(rat1)
    x2, y2 = get_numer(rat2), get_denom(rat2)
    return make(x1 * y2 + x2 * y1, y1 * y2)


def sub(rat1, rat2):
    x1, y1 = get_numer(rat1), get_denom(rat1)
    x2, y2 = get_numer(rat2), get_denom(rat2)
    return make(x1 * y2 - x2 * y1, y1 * y2)
