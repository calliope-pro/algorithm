# 典型90-042
# 9の倍数 -> 桁の合計が9の倍数である必要がある
# ある数字に対して0~9の1桁を追加すると考えればそれぞれは排反事象となる
# 1次のdpで解ける
import sys

ri = lambda: int(sys.stdin.readline())
mod1 = 10**9 + 7

n = ri()
if n % 9 != 0:
    print(0)
    exit()

dp = [0] * (n+1)  # dp[sum]はsumになる通り
for i in range(1, 10):
    dp[i] = 1
for i in range(1, n):
    for j in range(1, 10):
        if i+j > n:
            break
        dp[i+j] += dp[i]
        dp[i+j] %= mod1
print(dp[-1])
