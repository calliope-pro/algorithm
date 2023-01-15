# ABC258-D
# 制約的に1重ループは余裕
# 1ステージまでしかやらない時 ~ nステージ全てやる時それぞれの最小値を求めるといい
# 更に計算寮を減らすために累積和を使った
import sys

rm = lambda: map(int, sys.stdin.readline().split())
inf = float('inf')

n, x = rm()
time = inf
cum = 0
min_ = inf
for i in range(n):
    a, b = rm()
    min_ = min(b, min_)
    cum += a+b
    time = min(cum + min_*(x - i - 1), time)
print(time)
