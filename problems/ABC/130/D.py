# ABC136-D
# 累積和と二分探索を組み合わせる
# 右端の最小を見つけるだけでよい
import bisect
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
a = rl()
cum = [0] + list(itertools.accumulate(a))
ans = 0
for v in cum:
    ans += (n+1 - bisect.bisect_left(cum, v+k))
print(ans)
