# 典型90-032
# PyPy only
# 制約小さめなので、全探索してシミュレーションすればいい
import sys
import itertools

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n = ri()
a = [rl() for _ in range(n)]
m = ri()
xy = set(tuple(rm()) for _ in range(m))
ans = inf
for co in itertools.permutations(range(n)):
    tmp = 0
    for j, (idx_a, idx_b) in enumerate(zip(co, co[1:])):
        if (idx_a+1, idx_b+1) in xy or (idx_b+1, idx_a+1) in xy:
            break
        else:
            tmp += a[idx_a][j]
    else:
        tmp += a[co[-1]][-1]
        ans = min(tmp, ans)
if ans is inf:
    print(-1)
else:
    print(ans)
