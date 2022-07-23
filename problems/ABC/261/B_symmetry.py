import sys

if 'PyPy' not in sys.version:
    import numpy as np

rsl = lambda: list(sys.stdin.readline().rstrip())
ri = lambda: int(sys.stdin.readline())

n = ri()
def f(s):
    if s == '-' or s == 'D':
        return 0
    if s == 'L':
        return -1
    return 1
a = np.array([[f(i) for i in rsl()] for _ in range(n)])
print(bool((a + a.T).sum()) * 'in' + 'correct')