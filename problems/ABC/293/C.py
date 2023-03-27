# ABC293-C
# 制約は小さいので、全探索
# 下に行くタイミングを全探索することで効率よくできる
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

h, w = rm()
am = [rl() for _ in range(h)]
cnt = 0
directions = [0]*(h-1) + [1]*(w-1)
for co in itertools.combinations(range(h+w-2), r=h-1):
    passed = set([am[0][0]])
    co = set(co)
    x = 0
    y = 0
    for i in range(h+w-2):
        if i in co:
            x += 1
        else:
            y += 1
        passed.add(am[x][y])
    if len(passed) == (h+w-1):
        cnt += 1
print(cnt)
