import sys

rm = lambda: map(int, sys.stdin.readline().split())
mod2 = 998244353

n, m = rm()
dp = [1, 0]  # dp[n][i] n番目でi(0かどうか)のときの全通り (1人目が0であると仮定している)
for i in range(n-1):
    dp = [dp[1], (dp[0]*(m-1) + dp[1]*(m-2)) % mod2]
print(dp[-1] * m % mod2)
