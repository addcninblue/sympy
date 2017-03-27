#!/bin/env python3
total = 0
for i in range(1, 25, 2):
    for j in range(1, 25, 2):
        for k in range(1, 25, 2):
            if i + j + k == 25:
                total += 1
                print(f'({i})({j})({k})')
print(total)
