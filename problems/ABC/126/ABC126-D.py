# unsolved
import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.buffer.readline().rstrip()
rs = lambda: sys.stdin.buffer.readline().split()
ri = lambda: int(sys.stdin.buffer.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))

n = ri()
par = list(range(n))
rank = [0] * n
dist = [0] * n
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(x)
        return

def union(l, x1, y1): 
    x = find(x1)
    y = find(y1)
    if par[x] != par[y]:
        if rank[x] == rank[y]:
            rank[x] += 1
            par[y] = x
        elif rank[x] > rank(y):
            par[y] = x
        else:
            par[x] = y
    return

for _ in range(n-1):
    u, v, w = rl()

