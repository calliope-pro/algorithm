# 典型90-026
# 木 -> 二部グラフ -> 交互に偶奇を並べることができる
# dfs -> 偶奇のノードを分けて、要素数を比べればいいのだ
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10000000)

n = ri()
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = rm()
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

passed = [False] * n
is_even = [0] * n
is_even[0] = 1
nodes = [set(), set()]
def dfs(node=0):
    passed[node] = True
    nodes[is_even[node]].add(node+1)

    for next_node in edges[node]:
        if passed[next_node] == False:
            if is_even[node] == 0:
                is_even[next_node] = 1
            dfs(next_node)

dfs()
if len(nodes[0]) > len(nodes[1]):
    for _ in range(n//2):
        print(nodes[0].pop(), end=' ')
else:
    for _ in range(n//2):
        print(nodes[1].pop(), end=' ')
