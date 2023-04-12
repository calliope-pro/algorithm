# 典型90-008
# dp頭沸くなあ。
# 前の文字との整合性を考えればいい。なければスキップ。被ったら前までの文字の通り分だけ増える。新しい文字なら*1で同じ通りの数。
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())
mod1 = 10**9 + 7

atc = 'atcoder'
n = ri()
s = rr()
dp = [[0]*(len(atc) + 1) for _ in range(len(s) + 1)]  # dp[i][j] sのi文字目でatcoderのj文字目選択した通り
dp[0][0] = 1
for i in range(len(s)):
    c = s[i]
    if c not in atc:
        for j, v in enumerate(dp[i]):
            dp[i+1][j] = v
        continue

    atc_n = atc.index(c) + 1
    dp[i+1][atc_n] += dp[i][atc_n] + dp[i][atc_n-1]
    for j, v in enumerate(dp[i]):
        if j != atc_n:
            dp[i+1][j] = v
        dp[i+1][j] %= mod1

print(dp[-1][-1] % mod1)

