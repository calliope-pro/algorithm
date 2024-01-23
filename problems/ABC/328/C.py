# ABC328-C
# 隣り合う文字が存在している箇所を全て記録しておき、クエリに対して二分探索で答える
import bisect
import itertools
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, q = rm()
s = rr()
con = []
i = 0
for k, v in itertools.groupby(s):
    cnt = len(tuple(v))
    if cnt >= 2:
        con.extend(i+j+1 for j in range(cnt-1))
    i += cnt
for _ in range(q):
    l, r = rm()
    l_ = bisect.bisect_left(con, l)
    r_ = bisect.bisect_left(con, r)
    print(r_-l_)
