# ABC274-B
# numpyの転置を使った
import sys
import numpy as np

rsl = lambda: list(sys.stdin.readline().rstrip())
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
c = np.array([rsl() for _ in range(h)]).T
print(*(c == '#').sum(axis=1))
