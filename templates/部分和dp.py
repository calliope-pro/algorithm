import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: str(sys.stdin.buffer.readline().rstrip())
rs = lambda: map(str, sys.stdin.buffer.readline().split())
ri = lambda: int(sys.stdin.buffer.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))
inf = float('inf')
mod = 10**9+7

'''
5 1120
10 10 10 100 1000
# 部分和問題
n, a = rm()
li = rl()
dp = [[False]*(a+1) for _ in range(n+1)]
# dp[i][k] i番までの数でkが作れるか否か
dp[0][0] = True
for i in range(n):
    # 個数iは気にしなくていい実装
    for k in range(a+1):
        tmp = k-li[i]
        if tmp >= 0:
            dp[i+1][k] = dp[i][k] | dp[i][tmp]# | dp[i+1][k]
        else:
            dp[i+1][k] = dp[i][k]# | dp[i+1][k]
print(dp[n][a])
'''


'''
5 12
7 3 1 5 8
# 部分和数え上げ問題
n, a = rm()
li = rl()
dp = [[0]*(a+1) for _ in range(n+1)]
# dp[i][k] i番までの数でいくつkができるか
dp[0][0] = 1
for i in range(n):
    for k in range(a+1):
        tmp = k-li[i]
        if tmp >= 0:
            dp[i+1][k] += dp[i][k] + dp[i][tmp]
        else:
            dp[i+1][k] += dp[i][k]
print(dp[n][a])
'''


# 最小個数部分和問題
n, a, m = rm()
li = rl()
dp = [[inf]*(a+1) for _ in range(n+1)]
# dp[i][k] i番までの数でkができる最小の個数、無い場合はinf
# m個でaができるか
dp[0][0] = 0
for i in range(n):
    lii = li[i]
    for k in range(a+1):
        tmp = k - lii
        if tmp >= 0:
            dp[i+1][k] = min(dp[i][k], dp[i][tmp] + 1) # 後者はli[i]を選ぶため、+1が必要
        else:
            dp[i+1][k] = dp[i][k]
if dp[n][a] <= k:
    print('Yes')
else:
    print('No')







