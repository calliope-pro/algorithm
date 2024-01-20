# ABC337-A
# numpyで脳死でsum
import numpy as np
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
m = np.array([rl() for _ in range(n)]).sum(axis=0)
print("Takahashi" if m[0] > m[1] else "Aoki" if m[0] < m[1] else "Draw")
