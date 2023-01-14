# PAST011-E
# 制約が大きい -> 規則性に気付くことが大事
# 10**18とかのルートを取るならDecimalを使うと良い
# math.floorと**0.5だとWAになった
import sys
from decimal import Decimal

ri = lambda: int(sys.stdin.readline())

n = ri()
root = Decimal(n).sqrt() // 1
if n == root**2:
    print(root)
else:
    n_ = n - root**2
    if n_ >= (root + 1):
        print(n_ - root)
    else:
        print(root + 2 - n_)
