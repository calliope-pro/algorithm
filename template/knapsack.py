'''
6 15
6 5
5 6
6 4
6 6
3 5
7 2
'''
import sys
import math
import itertools
import collections
import numpy as np

rl = sys.stdin.readline

N, W = map(int, rl().split())
dp = [-1]*(W+1)
dp[0] = 0
for _ in range(N):
    w, v = map(int, rl().split())
    for i in range(W-w, -1, -1):
        dpi = dp[i]
        if dpi == -1:
            continue
        if dp[i+w] < dpi + v:
            dp[i+w] = dpi + v
print(max(dp))

