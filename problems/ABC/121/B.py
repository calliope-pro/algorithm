# ABC121-B
# numpyで内積だとして考える
import sys
import numpy as np

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m, c = rm()
b = np.array(rl())
cnt = 0
for _ in range(n):
    a = np.array(rl())
    if np.sum(a * b) > -c:
        cnt += 1
print(cnt)
