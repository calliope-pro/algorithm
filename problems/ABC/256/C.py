# ABC256-C
# 最後は確定することを考えると計算量がグーンと減らせる
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())

h1, h2, h3, w1, w2, w3 = rm()
cnt = 0
for co in itertools.product(range(1, 29), repeat=4):
    v13 = h1 - co[0] - co[1]
    v23 = h2 - co[2] - co[3]
    v31 = w1 - co[0] - co[2]
    v32 = w2 - co[1] - co[3]
    if min(v13, v23, v31, v32) <= 0:
        continue
    if h3 - v32 - v31 == w3 - v13 - v23 and w3 - v13 - v23 > 0:
        cnt += 1
print(cnt)
