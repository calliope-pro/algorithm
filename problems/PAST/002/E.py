# PAST002-E
# dfsとメモ化を使った(制約小さいためメモ化必要無いが)
import sys
from functools import lru_cache

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()

@lru_cache
def dfs(k, p):
    if al[k-1] == p:
        return 1
    return dfs(al[k-1], p) + 1

for av in al:
    print(dfs(av, av), end=' ')
