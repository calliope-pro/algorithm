# ABC248-C
# PyPy only
# ようやくACしたわ
# Cでdp出すなや
# 桁と合計の推移を計算
import sys

rm = lambda: map(int, sys.stdin.readline().split())
mod2 = 998244353

n, m, k = rm()
dp = [[0] * (n+1) for _ in range(n*m+2)]
dp[0][0] = 1
for i in range(n*m+2):
    for j in range(1, n+1):
        for dv in range(1, m+1):
            if i+dv < k or (j == n and i+dv == k):
                dp[i+dv][j] = (dp[i+dv][j] + dp[i][j-1]) % mod2
ans = 0
for r in dp:
    ans = (ans + r[-1]) % mod2
print(ans)
