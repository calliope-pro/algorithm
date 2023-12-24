# ABC310-C
# 正順・逆順の両方を確かめていく
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
set_ = set()
for _ in range(n):
    s = rr()
    if s not in set_ and s[::-1] not in set_:
        set_.add(s)
print(len(set_))
