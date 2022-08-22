# ABC265-D
# 累積和を使い、cum[i]+p, cum[i]+p+q, cum[i]+p+q+rが存在するか判定
import bisect
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, p, q, r = rm()
a = rl()
cum = [0] + list(itertools.accumulate(a))
for i in range(n+1):
    j = bisect.bisect_left(cum, cum[i] + p)
    if j > n or cum[i] + p != cum[j]:
        continue
    k = bisect.bisect_left(cum, cum[j] + q)
    if k > n or cum[j] + q != cum[k]:
        continue
    l = bisect.bisect_left(cum, cum[k] + r)
    if l > n or cum[k] + r != cum[l]:
        continue
    print('Yes')
    exit()
print('No')
