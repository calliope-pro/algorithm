# ABC297-B
# 計算量は多くないので、すべてのインデックスを強引に取得した
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
bi_left = s.index('B')
bi_right = s.index('B', bi_left+1)
ki = s.index('K')
ri_left = s.index('R')
ri_right = s.index('R', ri_left+1)
if bi_left&1 == bi_right&1:
    print('No')
    exit()
if ri_left < ki < ri_right:
    print('Yes')
else:
    print('No')
