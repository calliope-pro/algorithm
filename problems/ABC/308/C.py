# ABC308-C
# 小数なので、Decimalでゴリ押せ！
import sys
from decimal import Decimal

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
score = []
for i in range(n):
    a, b = rm()
    score.append((-Decimal('1.0000000000')*Decimal(a) / Decimal(a+b), i))
score.sort()
for s in score:
    print(s[1] + 1, end=' ')
