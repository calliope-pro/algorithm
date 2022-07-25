# PyPy only
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
x = rl()
bonus = {}
for _ in range(m):
    c, y = rm()
    bonus[c] = y

dp = [[0]*(n+1) for _ in range(n+1)]
# dp[i][j]: i回目までの試行,前に何連続表か
# dp[0][j]全て0

for i in range(1, n+1):
    v = x[i-1]
    for j in range(i+1):
        # 裏を出す場合
        dp[i][0] = max(dp[i-1][j], dp[i][0])
        # 表を出す場合
        dp[i][j] = dp[i-1][j-1] + v + bonus.get(j, 0)

print(max(dp[-1]))