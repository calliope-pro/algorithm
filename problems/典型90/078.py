# 典型90-078
# より小さい隣接頂点を格納するリストを作成するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
nodes = [[] for _ in range(n)]
for _ in range(m):
    a, b = sorted(rl())
    nodes[b-1].append(a)

ans = 0
for node in nodes:
    if len(node) == 1:
        ans += 1
print(ans)
