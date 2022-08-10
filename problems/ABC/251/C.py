# ABC251-C
# set使えばいい
import sys

rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())

n = ri()
max_score = 0
ans = None
set_ = set()
for i in range(1, n+1):
    s, t = rs()
    t = int(t)
    if s in set_:
        continue
    set_.add(s)
    if t > max_score:
        max_score = t
        ans = i
print(ans)
