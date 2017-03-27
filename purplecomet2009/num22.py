#!/bin/env python
from __future__ import division
from sympy import *
a, b, g, h = symbols('a b g h', positive=True)

solutions = {}
solutions.update(solve((a + 2 * b - 2, -(((a/2) + (b/2)) ** 2) + 1 - g, a*g - b*h, h - 1))[0])
H, G = solutions[h], solutions[g]
# print(solutions)
answer = H/G
print(simplify(H/G))
