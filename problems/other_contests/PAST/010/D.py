# PAST010-D
# np.maximum使って楽した
import sys
import numpy as np

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

t, n = rm()
p = [0]*n
for _ in range(t):
    p_ = rl()
    p = np.maximum(p, p_)
    print(sum(p))
