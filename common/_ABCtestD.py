import sys
import math
import itertools
import collections
import heapq
import re
from functools import reduce, lru_cache
from string import ascii_lowercase, ascii_uppercase
import queue
from decimal import Decimal, ROUND_HALF_UP
if 'PyPy' not in sys.version:
    import numpy as np
    from scipy.special import comb

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
rsl = lambda: list(sys.stdin.readline().split())
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rf = lambda: map(float, sys.stdin.readline().split())
rd = lambda: map(Decimal, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod1 = 10**9 + 7
mod2 = 998244353
al = ascii_lowercase
au = ascii_uppercase

# sys.setrecursionlimit(100000)

n, k, q = rm()
a = rl()
l = rl()
for lv in l:
    if a[lv-1] != n:
        if lv == k:
            a[lv-1] += 1
        elif a[lv] != a[lv-1] + 1:
            a[lv-1] += 1
print(*a)