# PAST013-F
# 数式から数の辺りをつける。
# 最後にちゃんと探索してしっかりとした結果を出す
import sys
import math
from decimal import Decimal

ri = lambda: int(sys.stdin.readline())
rd = lambda: map(Decimal, sys.stdin.readline().split())

n = ri()
a, b, c, d = rd()
x, *_ = rd()
t = a+b+c+d
sum_ = a + 2*b + 3*c + 4*d
l = max(math.ceil((x*t - sum_) / (1 - x)) - 5, 0)
for i in range(l, l+10):
    if (sum_ + i) / (t + i) <= x:
        print(i)
        exit()
