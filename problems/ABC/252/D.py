# ABC252-D
# i,j,kの組をjより小さいi, jより大きいkと仮定することで累積和に持ち込める
import sys
import itertools
import collections

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()
c = list(collections.Counter(a).items())
c.sort()
cum = tuple(itertools.accumulate(c, lambda a, b: a+b[1], initial=0))
ans = 0
for i in range(2, len(cum)-1):
    ans += cum[i-1] * (cum[i] - cum[i-1]) * (n - cum[i])
print(ans)
