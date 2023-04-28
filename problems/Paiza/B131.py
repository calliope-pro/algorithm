# Paiza-B131
# 別に最安値を考えたりする必要ないです。。楽です
# xの位置特に要らんていう。
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
am = [rl() for _ in range(n)]
ans = 0
q = ri()
x, y = 0, 0
for _ in range(q):
    r, s = rm()
    r -= 1
    s -= 1
    ans += abs(am[r][s] - am[r][y])
    x = r
    y = s
print(ans)
