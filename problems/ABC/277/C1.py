# ABC277-C
# 1度探索したところは探索しなくていい
# DFSをメモ化再帰で
import sys
import collections
from functools import lru_cache

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10000000)

n = ri()
nodes = collections.defaultdict(lambda: [])
passed = collections.defaultdict(lambda: False)
for _ in range(n):
    a, b = rm()
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

@lru_cache
def dfs(k=0):
    ans = k
    passed[k] = True
    for next_node in nodes[k]:
        if passed[next_node] == False:
            ans = max(dfs(next_node), ans)
    return ans
print(dfs() + 1)

