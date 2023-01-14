# ABC227-C
# PyPy only
# aとbの走査範囲は絞れる + a,bが決まればcの個数は自動的に求まる
import sys
import math

ri = lambda: int(sys.stdin.readline())

n = ri()
cnt = 0
for a in range(1, math.floor(pow(n, 1/3))+10):
    for b in range(a, math.floor(pow(n/a, 1/2))+10):
        c_cnt = math.floor(n / a / b)
        cnt += max(0, c_cnt - b + 1)
print(cnt)
