# PAST012-D
# グラフだから難しいかと思ったけど、クソ雑魚だ
# ただただ条件分岐するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
nodes = [set() for _ in range(n)]
for _ in range(m):
    u, v = rm()
    if u == v:
        print('No')
        exit()
    if u > n or v > n:
        print('No')
        exit()
    if v-1 in nodes[u-1]:
        print('No')
        exit()
    nodes[u-1].add(v-1)
    nodes[v-1].add(u-1)
print('Yes')
