# PAST005-C
# 愚直に変数に代入、余分な0を消すがゆえ、0がコーナーケース
# numpyの関数で楽に実装可能
import sys
from string import ascii_uppercase

ri = lambda: int(sys.stdin.readline())
au = ascii_uppercase

# 愚直
def f(n):
    if n == 0:
        print(0)
        exit()
    s = '0123456789' + au
    a = n // 36**2
    b = (n % 36**2) // 36
    c = n % 36
    print(f'{s[a]}{s[b]}{s[c]}'.lstrip('0'))

# numpy実装
def f(n):
    from numpy import base_repr
    print(base_repr(n, 36))

n = ri()
f(n)
