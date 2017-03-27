#!/bin/env python
from __future__ import division
from sympy import *
a, b = symbols('a b')
eq1 = a ** 2 + b ** 2 - 5
eq2 = a ** 3 + b ** 3 - 7

solutions = solve_poly_system([eq1, eq2], a, b)
maximum = -100000
for (x, y) in solutions:
    total = x + y
    maximum = max(maximum, re(total))

print(maximum) # answer is 57
