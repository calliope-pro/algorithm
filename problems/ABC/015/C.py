# ABC015-C
# 制約が小さいので愚直にシミュレート
import sys
import itertools
from operator import xor
from functools import reduce

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
t = [rl() for _ in range(n)]
for t_li in itertools.product(*t):
    if reduce(xor, t_li) == 0:
        print('Found')
        exit()
print('Nothing')
