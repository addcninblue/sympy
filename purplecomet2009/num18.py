#!/bin/env python
from __future__ import division
from sympy import *
BD, AD, BC, AB, CD, AC = symbols('BD AD BC AB CD AC', positive=True)

# solutions are a dictionary of line lengths
# _ is a point
# line__ is a line connecting those two points
# lineSeg__ is a line segment connecting those two points
solutions = {}
solutions.update(solve((14**2 * BD + BC ** 2 * AD - AD*BD*28 - 28*CD**2, AD + BD - 28, AD**2 + 10**2 - 14 ** 2, BD**2 + 10**2 - BC ** 2))[0])
solutions[AC] = 14
solutions[AB] = 28

# construct triangle with 3 given side lengths
ABC = Triangle(sss=(solutions[AB], solutions[BC], solutions[AC]))

# assign coordinates to A, B, C
A, B, C = ABC.vertices

# get line segments AE and CD
lineSegAE = ABC.bisectors()[A]
lineSegCD = ABC.altitudes[C]

# get point G from intersection of AE and CD
G = lineSegAE.intersection(lineSegCD)[0]

# get line BG
lineBG = Line(B, G)

# get line AC
lineAC = Line(A, C)

# get F from intersection of BG and AC
F = lineBG.intersection(lineAC)[0]

# print distance from F to C
# `simplify` simplifies fraction
# `sqrtdenest` denests square roots
print(sqrtdenest(simplify(F.distance(C))))

# solution:
# k = 770
# m = 196
# p = 6
# n = 43
