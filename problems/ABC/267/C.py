# ABC267-C
# 累積和、前項との差を考えて数学的にシミュレートする
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
a = rl()
cum = list(itertools.accumulate(a))
ans = sum(a[i]*(i+1) for i in range(m))
tmp = ans
for i in range(n-m):
    tmp = tmp - (cum[i+m-1] - cum[i]) + m*a[i+m] - a[i]
    ans = max(tmp, ans)
print(ans)
