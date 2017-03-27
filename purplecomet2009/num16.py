#!/bin/env python3
from math import cos, sin
a = cos(1/1000) + 1j * sin(1/1000)
for i in range(1, 1000):
    if (a ** i).imag >= 0.5:
        print(i)
        break
