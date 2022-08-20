# ABC040-C
# 典型的なメモ化再帰・dp
import sys
from functools import lru_cache

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()

# メモ化再帰
sys.setrecursionlimit(10000000)
@lru_cache(maxsize=None)
def f(idx):
    if idx == 0:
        return 0
    if idx == 1:
        return abs(a[1] - a[0])
    return min(f(idx-1) + abs(a[idx] - a[idx-1]), f(idx-2) + abs(a[idx] - a[idx-2]))

# dp
def f(idx):
    av, bv = 0, abs(a[1] - a[0])
    for i in range(2, idx+1):
        av, bv = bv, min(av + abs(a[i] - a[i-2]), bv + abs(a[i] - a[i-1]))
    return bv

print(f(n-1))
