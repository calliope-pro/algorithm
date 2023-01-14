# ABC220-D
# dpを使うしかない
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))
mod2 = 998244353

n = ri()
al = rl()
dp = [[0] * 10 for _ in range(n)]  # dp[i][j] i回の操作後左端がjである時の操作手順数
dp[0][al[0]] = 1
for i in range(1, n):
    for j in range(10):
        f = (al[i] + j) % 10
        g = (al[i] * j) % 10
        dp[i][f] += dp[i-1][j]
        dp[i][f] %= mod2
        dp[i][g] += dp[i-1][j]
        dp[i][g] %= mod2
print(*dp[-1], sep='\n')
