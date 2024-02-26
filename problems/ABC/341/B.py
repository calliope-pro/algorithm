# ABC341-B
# 最大でいくらの硬貨を得られるか繰り返していくだけ
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
for i in range(n-1):
    s, t = rm()
    al[i+1] += (al[i] // s) * t
print(al[-1])
