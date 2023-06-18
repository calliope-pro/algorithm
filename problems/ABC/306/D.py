# ABC306-D
# DはdpのD!
# これぐらいだと数分でできるようになってきた。
# 前の状態から不変のときも初提出で忘れないようにしたい。
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
inf = float('inf')

n = ri()
dp = [[0]*2 for _ in range(n+1)]  # dp[n_][state_] <- 最大値
dp[0][1] = -inf
for i in range(n):
    x, y = rm()
    if x == 0:
        dp[i+1][0] = max(dp[i][0] + y, dp[i][1] + y, dp[i][0])
        dp[i+1][1] = dp[i][1]
    else:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = max(dp[i][0] + y, dp[i][1])
print(max(dp[-1]))
