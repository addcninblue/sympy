#!/bin/env python
from itertools import permutations
allperms = sorted(''.join(chars) for chars in set(permutations('WWWWWWWMMMMM')))
print(allperms)
