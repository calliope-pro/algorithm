# ABC327-C
# numpyのfancy indexを使うと非常に楽
import sys
import numpy as np

rl = lambda: list(map(int, sys.stdin.readline().split()))

am = np.array([rl() for _ in range(9)], dtype=np.int64)
for i in range(9):
    if len(set(am[i, :])) != 9:
        print("No")
        exit()
    if len(set(am[:, i])) != 9:
        print("No")
        exit()
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        if len(set(am[i:i+3, j:j+3].flatten())) != 9:
            print("No")
            exit()
print("Yes")
