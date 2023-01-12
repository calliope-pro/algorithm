# PAST004-D
# 左と右に行う操作の最低回数は決まっている
# 最低回数以降はどちらの操作でもいいので、今回はBの操作にどれだけ加算するかを計算した
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
g = list((g_[0], len(list(g_[1]))) for g_ in itertools.groupby(s))

left = 0
if g[0][0] == '.':
    left = g[0][1]
right = 0
if g[-1][0] == '.':
    right = g[-1][1]

cnt = 0
for g_ in g:
    if g_[0] == '.':
        cnt = max(g_[1], cnt)
print(left, right + max(0, cnt-left-right))
