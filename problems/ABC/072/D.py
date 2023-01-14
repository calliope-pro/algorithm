# ABC072-D
# どんな隣同士でも、どちらかが条件に合致してない -> swapすれば条件に合致する性質を見抜く
# 前から条件合致してないならswapをしていくだけになる
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
pl = rl()
cnt = 0
for i in range(1, n):
    if i == pl[i-1]:
        cnt += 1
        pl[i-1], pl[i] = pl[i], pl[i-1]
print(cnt + int(pl[n-1]==n))
