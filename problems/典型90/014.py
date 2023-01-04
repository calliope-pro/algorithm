# 典型90-014
# 同要素数なので、交差させるよりランク数が等しい差の方が小さくなる
# そのため、ソートしてランクごとに絶対値を取る
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
al.sort()
bl = rl()
bl.sort()
ans = 0
for av, bv in zip(al, bl):
    ans += abs(av-bv)
print(ans)
