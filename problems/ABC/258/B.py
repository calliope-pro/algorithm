# ABC258-B
# 問題の誤読に気をつけよう
# 全部のマスでそれぞれの方向に1直線でシミュレートをする
import sys
from functools import lru_cache

rsl = lambda: list(sys.stdin.readline().rstrip())
ri = lambda: int(sys.stdin.readline())

n = ri()
a = [rsl() for _ in range(n)]

dxdy = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

ans = ''
for i in range(n):
    for j in range(n):
        for dx, dy in dxdy:
            tmp = a[i][j]
            for _ in range(n-1):
                i = (i + dx) % n
                j = (j + dy) % n
                tmp += a[i][j]
            ans = max(tmp, ans)
print(ans)