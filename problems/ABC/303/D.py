# ABC303-D
# DはdpのD!
# on, offでの最短時間の遷移を考える
# 時間的にRLEした方がいいと思ったけど要らんかったぽいな
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

x, y, z = rm()
s = rr()
rle = itertools.groupby(s)
ans = [float('inf'), 0]  # on, off, onをinfにすると初期状態をわざわざ計算しなくていい
for c, li in rle:
    cnt = len(tuple(li))
    if c == 'A':
        tmp0 = min(ans[0], ans[1] + z) + x*cnt
        tmp1 = min(ans[0] + z, ans[1]) + y*cnt
    else:
        tmp0 = min(ans[0], ans[1] + z) + y*cnt
        tmp1 = min(ans[0] + z, ans[1]) + x*cnt
    ans = [tmp0, tmp1]
print(min(ans))
