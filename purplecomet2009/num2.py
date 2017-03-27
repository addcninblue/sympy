#!/bin/env python
from __future__ import division
from sympy import *
septagon = RegularPolygon(Point(0,0), 1, n = 7)
a, b, c, d, e, f, g = septagon.vertices
l1 = Line(a, e)
l2 = Line(c, g)
angle = l1.angle_between(l2)
ans = (angle * 360 * 7 / (2 * pi)).evalf() + 7
print(round(ans)) # 727
