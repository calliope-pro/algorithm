# ABC-057
# 因数分解と同じ。ルートを考えると楽。
# 更に大きい方から探索することで速い
import sys
import math

ri = lambda: int(sys.stdin.readline())

n = ri()
for i in range(math.ceil(n**0.5), 0, -1):
    if n % i == 0:
        print(len(str(n//i)))
        break
