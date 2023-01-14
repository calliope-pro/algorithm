# ABC227-B
# 制約が小さいので、あり得る面積は全て羅列
# 有り得ない数の人をカウンターで数える
import sys
import collections
import numpy as np

rm = lambda: map(int, sys.stdin.readline().split())

rm()
s = collections.Counter(rm())
cnt = 0
for a, b in np.ndindex(250, 250):
    if a == 0 or b == 0:
        continue
    s[4*a*b + 3*a +3*b] = 0
print(sum(s.values()))