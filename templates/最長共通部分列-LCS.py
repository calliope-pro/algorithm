import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.buffer.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

s = rr()
t = rr()
lens = len(s)
lent = len(t)
dp = [[0]*lent for _ in range(lens)]
for i in range(lens-1):
    for j in range(lent-1):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j]+1)
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
print(dp[lens-1][lent-1])