# ABC304-D
# ソートされたリスト -> 二分探索使えそう
# p, qから存在する群のidを作成できればいい
# p以上の最小x座標とq以上の最小y座標をそのidにすればいい
import bisect
import sys
import collections

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

w, h = rm()
n = ri()
pq = [rl() for _ in range(n)]
a = ri()
al = rl() + [w]
b = ri()
bl = rl() + [h]
counter = collections.Counter()
for p, q in pq:
    x_idx = bisect.bisect_left(al, p)
    y_idx = bisect.bisect_left(bl, q)
    counter[(x_idx, y_idx)] += 1
max_ = 0
min_ = inf
if len(counter) < (a+1) * (b+1):
    min_ = 0
for k, v in counter.items():
    max_ = max(v, max_)
    min_ = min(v, min_)
print(min_, max_)
