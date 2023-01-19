# ABC024-C
# 制約が小さいので、2重ループでいい
# 貪欲的に値を更新していくことを考えればよい
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, d, k = rm()
lr = [tuple(rm()) for _ in range(d)]
st = [rl() for _ in range(k)]
ans = [None] * k
for days, (l, r) in enumerate(lr, 1):
    for idx, (s, t) in enumerate(st):
        if s < t and l <= s <= r:
            s = min(r, t)
            st[idx][0] = s
        elif s > t and l <= s <= r:
            s = max(l, t)
            st[idx][0] = s
        if s == t and ans[idx] is None:
            ans[idx] = days
print(*ans, sep='\n')
