'''
8
1 5
2 4
3 5
1 4
3 4
1 3
1 2
3 5
'''
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
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

n = ri()
li = [rl() for _ in range(n)]

cnt_list = [0] * 6
for lis in li:
    s, e = lis
    cnt_list[s-1] += 1
    cnt_list[e] -= 1

ma = 0
tmp = 0
for i in cnt_list:
    tmp += i
    ma = max(tmp, ma)
else:
    print(ma)



