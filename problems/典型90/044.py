# 典型90-044
# PyPy only
# 先頭・末尾使うやつはdeque使ってごり押し
import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, q = rm()
al = rl()
d = collections.deque(al)
for _ in range(q):
    t, x, y = rm()
    if t == 1:
        d[x-1], d[y-1] = d[y-1], d[x-1]
    elif t == 2:
        d.appendleft(d.pop())
    elif t == 3:
        print(d[x-1])
