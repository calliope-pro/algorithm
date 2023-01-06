# 典型90-064
# 初期条件と階差の変化を検討すると良い
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, q = rm()
al = rl()
diff = [j-i for i, j in zip(al, al[1:])]
ans = sum(abs(i) for i in diff)
for _ in range(q):
    l, r, v = rm()
    if l-2 >= 0:
        ans -= abs(diff[l-2])
        diff[l-2] += v
        ans += abs(diff[l-2])
    if r-1 <= n-2:
        ans -= abs(diff[r-1])
        diff[r-1] -= v
        ans += abs(diff[r-1])
    print(ans)
