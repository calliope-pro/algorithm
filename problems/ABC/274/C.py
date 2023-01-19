# ABC274-C
# 問題が読みにくいったらありやしない
# 制約がそこまで大きくない + キャッシュでメモ化させたため、再帰にした
import sys
from functools import lru_cache

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
@lru_cache
def f(x):
    if x == 1:
        return 0
    parent_idx = x//2 - 1
    return f(al[parent_idx]) + 1

for i in range(1, 2*n + 2):
    print(f(i))
