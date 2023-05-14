# PAST013-B
# 制約小さいし、decimalでいける
import sys
from decimal import Decimal

rd = lambda: map(Decimal, sys.stdin.readline().split())

a, b, c, d = rd()
if a/b == c/d:
    print('=')
elif a/b > c/d:
    print('>')
else:
    print('<')
