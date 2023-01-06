# 典型90-069
# 条件分岐をしっかりと見極める
# pow関数を使って累乗の計算を軽くする
import sys

rm = lambda: map(int, sys.stdin.readline().split())
mod1 = 10**9 + 7

n, k = rm()
if k == 1:
    if n > 1:
        print(0)
    else:
        print(1)
    exit()
if k == 2:
    if n > k:
        print(0)
    else:
        print(2)
    exit()

if n > 2:
    print((k*(k-1)*pow(k-2, n-2, mod1)) % mod1)
if n == 2:
    print((k * (k-1)) % mod1)
if n == 1:
    print(k)
