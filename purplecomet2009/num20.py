#!/bin/env python
from itertools import permutations
from sympy import *


def isWoman(i):
    for key, c in enumerate(i):
        if c == 'M':
            if key == 0:
                if i[1] != 'W':
                    return False
            elif key == len(i) - 1:
                if i[len(i) - 2] != 'W':
                    return False
            else:
                if i[key - 1] != 'W' and i[key + 1] != 'W':
                    return False
    return True


def main():
    allperms = sorted(''.join(chars) for chars in set(permutations('WWWWWWWMMMMM')))
    print(len(allperms))

    count = 0
    for i in allperms:
        if isWoman(i):
            count += 1
    print(count)
    print(f'{count}/{len(allperms)}')
    ans = (len(allperms) + count) / (gcd(len(allperms), count))
    print(ans) # 287


main()
