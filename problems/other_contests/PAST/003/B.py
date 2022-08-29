# PAST003-B
# 愚直にシミュレート
# defaultdict使って楽した
import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

N, M, q = rm()
d = collections.defaultdict(lambda: N)
solved = [set() for _ in range(N)]
for _ in range(q):
    s = rl()
    if len(s) == 2:
        n = s[1]
        ans = 0
        for v in solved[n-1]:
            ans += d[v]
        print(ans)
    else:
        n, m = s[1:]
        solved[n-1].add(m)
        d[m] -= 1
