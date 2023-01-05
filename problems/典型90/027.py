# 典型90-027
# 集合使うと楽
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
set_ = set()
for i in range(n):
    s = rr()
    if s not in set_:
        print(i+1)
        set_.add(s)
