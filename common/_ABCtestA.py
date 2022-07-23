import sys
import math
import itertools
import collections
import heapq
import re
import queue
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
from functools import reduce, lru_cache
from string import ascii_lowercase, ascii_uppercase

if 'PyPy' not in sys.version:
    import numpy as np
    from scipy.special import comb

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
rsl = lambda: list(sys.stdin.readline().rstrip())
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


