#!/bin/env python
from __future__ import division
from sympy import *

# original solution that employed partial derivatives.
# did NOT work
# x, y = symbols('x y', positive=True)
# equation = sqrt((x+1)**2 + (y-2)**2) + sqrt((x-3)**2 + (y+4)**2) + sqrt((x-5)**2 + (y+6)**2) + sqrt((x+2)**2 + (y-8)**2)
# print(equation)
# diffx = equation.diff(x)
# diffy = equation.diff(y)
# print(diffx)
# print(diffy)
# solutions = solve(diffy)
# print(solutions)

# somehow, assuming that the minimum will be the intersection of
# two lines actually works
A = Point(-1, 2)
B = Point(3, -4)
C = Point(5, -6)
D = Point(-2, 8)

l1 = Line(A, C)
l2 = Line(B, D)

P = l1.intersection(l2)[0]

x, y = P
dist = sqrt((x+1)**2 + (y-2)**2) + sqrt((x-3)**2 + (y+4)**2) + sqrt((x-5)**2 + (y+6)**2) + sqrt((x+2)**2 + (y-8)**2)
print(dist)
