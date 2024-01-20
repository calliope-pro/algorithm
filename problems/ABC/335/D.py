# ABC335-D
# Python only
# numpyで回転 + 代入を強引にしたw
import sys

if "PyPy" not in sys.version:
    import numpy as np

ri = lambda: int(sys.stdin.readline())

n = ri()
m = np.zeros((n, n), dtype=np.int64)
for i in range(n // 2):
    for j in range(4):
        if j == 0:
            m[i, i] = m[i, i - 1] + 1
            m[i, i : n - i] = np.arange(m[i, i], m[i, i] + n - 2 * i)
        elif j == 3:
            m[i, i : n - i - 1] = np.arange(m[i, i], m[i, i] + n - 2 * i - 1)
        else:
            m[i, i : n - i] = np.arange(m[i, i], m[i, i] + n - 2 * i)
        m = np.rot90(m)
for i, l in enumerate(m):
    if i == n // 2:
        l = list(l)
        l[n // 2] = "T"
        print(*l)
    else:
        print(*l)
