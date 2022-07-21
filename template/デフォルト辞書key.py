# ABC061 C
import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce
from string import ascii_lowercase, ascii_uppercase

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
rsl = lambda: list(sys.stdin.readline().split())
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rf = lambda: map(float, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod1 = 10**9 + 7
# mod2 = 
al = ascii_lowercase
au = ascii_uppercase

n, k = rm()
d = collections.defaultdict(lambda:0) # これ使いやすいな
for _ in range(n):
    a, b = rm()
    d[a] += b
for i, v in sorted(d.items(), key=lambda x:x[0]):
    k -= v
    if k <= 0:
        print(i)
        exit()
    













