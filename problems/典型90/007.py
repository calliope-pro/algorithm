# 典型90-007
# 二分探索をすると良い
import bisect
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n = ri()
a = rl()
a.sort()
a.append(inf)
q = ri()
for _ in range(q):
    b = ri()
    idx_r = bisect.bisect(a, b)
    ans = min(abs(a[idx_r] - b), abs(a[idx_r-1] - b))
    print(ans)
