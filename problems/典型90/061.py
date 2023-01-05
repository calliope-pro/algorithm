# 典型90-061
# 先頭と末尾に挿入 -> dequeを使うことを検討
import sys
import collections

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

q = ri()
d = collections.deque()
for _ in range(q):
    t, x = rm()
    if t == 1:
        d.appendleft(x)
    if t == 2:
        d.append(x)
    if t == 3:
        print(d[x-1])
