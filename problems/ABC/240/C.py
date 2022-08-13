# ABC240-C
# dp(組み込みキャッシュ利用版も)
import sys
from functools import lru_cache

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, x = rm()
ab = [rl() for _ in range(n)]

# dp使わない実務的実装
@lru_cache(maxsize=None)
def f(t=0, now=0):
    if t == n:
        return now == x
    return f(t+1, now+ab[t][0]) or f(t+1, now+ab[t][1])

# dpによる実装
dp = [[None]*10001 for _ in range(101)]
def f(t=0, now=0):
    if dp[t][now] is not None:
        return dp[t][now]

    if t == n:
        dp[t][now] = now == x
        return now == x
    dp[t][now] = f(t+1, now+ab[t][0]) or f(t+1, now+ab[t][1])
    return dp[t][now]

print('NYoe s'[f()::2])
