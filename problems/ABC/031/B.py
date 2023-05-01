# ABC031-B
# ループと条件分岐するだけ
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

l, h = rm()
n = ri()
for _ in range(n):
    t = ri()
    if t > h:
        print(-1)
    elif t < l:
        print(l-t)
    else:
        print(0)
