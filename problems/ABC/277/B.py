# ABC277-B
# 条件分岐、アーリーリターンで記述量減らす
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = set()
for _ in range(n):
    s_ = rr()
    if s_[0] not in 'HDCS':
        print('No')
        exit()
    if s_[1] not in 'A23456789TJQK':
        print('No')
        exit()
    s.add(s_)
if len(s) != n:
    print('No')
else:
    print('Yes')
