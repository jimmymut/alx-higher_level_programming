#!/usr/bin/python3
def pow(a, b):
    power = 1
    if b < 0:
        b = -b
        for i in range(b):
            power = float(power) / a
    elif b == 0:
        power = 1
    else:
        for i in range(b):
            power *= a
    return power
