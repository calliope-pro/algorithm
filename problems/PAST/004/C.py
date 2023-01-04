# PAST004-C
# 畳み込み演算を用いると数学的にできる(思ったよりだるい)
import sys
import numpy as np
from scipy.signal import convolve2d

rsl = lambda: list(sys.stdin.readline().rstrip())
rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
s = np.array([rsl() for _ in range(n)]) == '#'
s = s + 0
ans = convolve2d(s, [[1, 1, 1],[1, 1, 1],[1, 1, 1]], 'same')
for li in ans:
    print(''.join(map(str, li)))
