# ABC211-C
# 典型的なdp
# 初期条件をしっかりと見極める
import sys

rr = lambda: sys.stdin.readline().rstrip()
mod1 = 10**9 + 7

s = rr()
CHOKUDAI = 'chokudai'
# dp[i][j] sのi文字目までで、atcoderのj文字目まで合致する通り
# dp[i][0]は全て1通りとする初期条件
dp = [[1]+[0]*len(CHOKUDAI) for _ in range(len(s)+1)]
for i in range(len(s)):
    for j in range(len(CHOKUDAI)):
        dp[i+1][j+1] = dp[i][j+1]
        if s[i] == CHOKUDAI[j]:
            dp[i+1][j+1] += dp[i][j]
print(dp[-1][-1] % mod1)
