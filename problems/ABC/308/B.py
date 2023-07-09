# ABC308-B
# 制約が小さいので、dictにすべての対応関係保存すればいい
import sys

rs = lambda: sys.stdin.readline().split()
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
cl = rs()
dl = rs()
pl = rl()
d = {}
for i, dv in enumerate(dl, 1):
    d[dv] = pl[i]
ans = 0
for cv in cl:
    ans += d.get(cv, pl[0])
print(ans)
