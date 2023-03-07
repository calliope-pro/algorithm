# ABC290-A
# npのファンシーインデックスを使って短くした
import sys

if 'PyPy' not in sys.version:
    import numpy as np

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
al = np.array(rl())
bl = np.array(rl()) - 1
print(al[bl].sum())
