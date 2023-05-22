# ABC302-D
# ソートして、+dまでの範囲に値が含まれているかどうかを調べればソート除いて、NlogN
# 尺取りで2Nでも充分速い
import bisect
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m, d = rm()
al = rl()
al.sort()
bl = rl()
bl.sort()
ans = -1
for av in al:
    idx = max(0, bisect.bisect_right(bl, av+d)-1)
    if abs(av - bl[idx]) <= d: 
        ans = max(av + bl[idx], ans)
print(ans)
