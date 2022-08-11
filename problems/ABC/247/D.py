import sys
import collections

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

q = ri()
d = collections.deque([])
for _ in range(q):
    n, *order = rm()
    if n == 1:
        d.append([order[0], order[1]])
    else:
        ans = 0
        c = order[0]
        while True:
            v = d.popleft()
            if c - v[1] > 0:
                ans += v[0] * v[1]
                c -= v[1]
            else:
                ans += v[0] * (c)
                d.appendleft([v[0], v[1] - c])
                break
        print(ans)
