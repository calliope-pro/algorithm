# ABC173-C
# 2次bit全探索
import sys
from itertools import combinations
import numpy as np

rm = lambda: map(int, sys.stdin.readline().split())
rr = lambda: sys.stdin.readline().rstrip()

h, w, k = rm()
li = np.array([np.array(list(rr())) for _ in range(h)])
cnt = 0

for i in range(h+1):
    for a in np.array(list(combinations(li, i))):
        a = a.T
        for j in range(w+1):
            for b in np.array(list(combinations(a, j))):
                t = np.count_nonzero(b == '#')
                if t == k:
                    cnt += 1
print(cnt)
