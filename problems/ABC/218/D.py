# ABC218-D
# 対角の点 -> 残りの2点の組み合わせが決まる -> これを全探索
# 対角の組み合わせは2つある -> 最後に2で割る
import sys
import collections

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
xy = collections.Counter()
for _ in range(n):
    x, y = rm()
    xy[(x, y)] += 1
nodes_cnt = len(xy)
xy_set = list(xy.keys())
cnt = 0
for i in range(nodes_cnt-1):
    for j in range(i+1, nodes_cnt):
        x1, y1 = xy_set[i]
        x2, y2 = xy_set[j]
        if x1 != x2 and y1 != y2:
            cnt += xy[(x1, y2)] * xy[(x2, y1)]
print(cnt//2)
