# ABC265-A
# 3個セットを何個買うかを決定させる
import sys

rm = lambda: map(int, sys.stdin.readline().split())
inf = float('inf')

x, y, n = rm()
ans = inf
for i in range(n//3 + 1):
    x_cnt = n - i*3
    ans = min(ans, i*y + x_cnt*x)
print(ans)
