# ABC253-D
# 簡単。絶対D問題じゃない。。包除原理というが、いたって普通な原理。。
# pythonなので、大きい数でも強引に計算できる。
import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())

n, a, b = rm()
a_cnt = n//a
a_max = a_cnt * a
b_cnt = n//b
b_max = b_cnt * b
gcd = math.gcd(a, b)
lcm = a*b//gcd
lcm_cnt = n//lcm
lcm_max = lcm_cnt * lcm
print((1+n)*n//2 - (a + a_max)*a_cnt//2 - (b + b_max)*b_cnt//2 + (lcm + lcm_max)*lcm_cnt//2)
