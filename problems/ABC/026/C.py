# ABC026-C
# 制約が小さかった+単調的なので貪欲法でシミュレート
import sys

ri = lambda: int(sys.stdin.readline())
inf = float('inf')

n = ri()
b = [[inf, 0, n]] + [[inf, 0, ri()-1] for _ in range(1, n)]
# [部下のmin給料, 部下のmax給料, 上司のidx]
for bv in reversed(b):
    idx = bv[-1]
    if idx == n:
        print(b[0][0]+b[0][1]+1)
        exit()
    if bv[1] == 0:
        bv[0] = 0
    b[idx][0] = min(bv[1]+bv[0]+1, b[idx][0])
    b[idx][1] = max(bv[1]+bv[0]+1, b[idx][1])
