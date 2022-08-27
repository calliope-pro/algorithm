# ABC266-D
# dpを使えばいい、序盤行ける座標が限られていることに注意
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
txa = {}
for _ in range(n):
    t, x, a = rm()
    txa[(t, x)] = a
# dp = [t][i]  # t秒時点でi番目の穴に居る時の最大値
dp = [[0]*(5) for _ in range(10**5+2)]
for t in range(10**5+1):
    for i in range(min(5, t+2)):
        if i == 0:
            dp[t+1][i] = max(dp[t][i+1], dp[t][i])
        elif i == 4:
            dp[t+1][i] = max(dp[t][i], dp[t][i-1])
        else:
            dp[t+1][i] = max(dp[t][i+1], dp[t][i], dp[t][i-1])
        dp[t+1][i] += txa.get((t+1, i), 0)

print(max(dp[-1]))
