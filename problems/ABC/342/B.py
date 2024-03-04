# ABC342-B
# ナイーブに全部の場所を探索
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
pl = rl()
q = ri()
for _ in range(q):
    a, b = rm()
    if pl.index(a) < pl.index(b):
        print(a)
    else:
        print(b)
