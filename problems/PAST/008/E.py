# PAST008-E
# 制約が10**5なので、ソートで間に合う
# collections.defaultdict使ってそれぞれの色に対する最低値を得る
# 最後に最低値をソートして合計
import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n, k = rm()
cl = rl()
pl = rl()
d = collections.defaultdict(lambda: inf)
for cv, pv in zip(cl, pl):
    d[cv] = min(pv, d[cv])
if len(d) < k:
    print(-1)
    exit()
print(sum(sorted(d.values())[:k]))
