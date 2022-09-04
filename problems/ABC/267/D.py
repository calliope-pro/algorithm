# ABC267-D
# dp、初期値の設定とiとjの関係性をしっかりと定義しておかないと挙動不審になる
# 未定義の組み合わせは-infとした
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n, m = rm()
a = rl()
dp = [[0]+[-inf]*(m) for _ in range(n)]
# dp[i][j], a[i]までj個使ったときの最大値
dp[0][0] = 0
dp[0][1] = a[0]
for i in range(n-1):
    for j in range(m):
        if i+1 >= j:
            dp[i+1][j+1] = max(dp[i][j] + (j+1)*a[i+1], dp[i][j+1])
print(dp[-1][-1])
