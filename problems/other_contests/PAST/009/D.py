# PAST009-D
# 複数キーソートする
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()
b = rl()
scores = [(-av-bv, -av, i+1) for i, (av, bv) in enumerate(zip(a, b))]
scores.sort()
for i in range(n):
    print(scores[i][-1], end=' ')
