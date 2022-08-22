# ABC265-B
# 愚直にシミュレート
# 計算量を落とすために辞書を用いた
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m , t = rm()
a = rl()
xy = dict()
for _ in range(m):
    x, y = rm()
    xy[x-1] = y
for i, av in enumerate(a, 1):
    t -= av
    if t <= 0:
        print('No')
        exit()
    t += xy.get(i, 0)
print('Yes')
