# ABC226-D
# 傾きが必要ということ -> 順列と集合を使うと計算量落としつつ楽になる
import sys
import math
import itertools

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
xy = [tuple(rm()) for _ in range(n)]
set_ = set()
for xy1, xy2 in itertools.permutations(xy, 2):
    x1, y1 = xy1 
    x2, y2 = xy2
    x_diff = x2-x1
    y_diff = y2-y1
    g = math.gcd(x_diff, y_diff)
    set_.add((x_diff//g, y_diff//g))
print(len(set_))
