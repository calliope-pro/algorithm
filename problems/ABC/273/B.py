# ABC273-B
# 桁指定の四捨五入はDecimalが楽
import sys
from decimal import Decimal, ROUND_HALF_UP

rd = lambda: map(Decimal, sys.stdin.readline().split())

x, k = rd()
k = int(k)
for i in range(k):
    x = x.quantize(Decimal(f'1e{i+1}'), ROUND_HALF_UP)
print(int(x))
