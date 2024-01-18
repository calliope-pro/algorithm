# ABC336-B
# 2で割れる回数を数えるだけ、bit演算すると楽
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
for i in range(10**10):
    if n & 1:
        print(i)
        break
    n >>= 1
