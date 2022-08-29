# PAST003-C
# logを使うと数学的で楽
# 2**31が10**9を超えることを利用して愚直にシミュレートでもok
import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())

a, r, n = rm()
print('large' if (n-1)*math.log(r) > math.log(10**9 / a) else a * r**(n-1))
