# ABC112-C
# 制約的に全探索*検証がN^3でできるからやるだけ
# sampleとして使える条件をしっかりと考える
import sys
import itertools

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
xyh = []
sample = None
for _ in range(n):
    row = rl()
    if sample is None and row[-1] > 0:
        sample = row
    xyh.append(row)
for cx, cy in itertools.product(range(101), repeat=2):
    x, y, h = sample
    h_test = abs(cx-x) + abs(cy-y) + h
    for (x, y, h) in xyh:
        if max(h_test - abs(cx-x) - abs(cy-y), 0) != h:
            break
    else:
        print(cx, cy, h_test)
        exit()
