# ABC248-D
# N + QlogNで解ける
# 最初に各数字の出現位置を記録しておき、クエリごとに二分探索で範囲内の個数を数える
import bisect
import sys
import collections

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
m = collections.defaultdict(list)
for i, ai in enumerate(al):
    m[ai].append(i+1)
q = ri()
for _ in range(q):
    l, r, x = rm()
    l_ = bisect.bisect_left(m[x], l)
    r_ = bisect.bisect_right(m[x], r)
    print(r_ - l_)
