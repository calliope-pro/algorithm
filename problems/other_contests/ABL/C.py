# ABL-C
# dfs使って連結成分の個数を数え上げる -> 個数-1の経路があれば全て通れる
import sys

rm = lambda: map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10000000)

n, m = rm()
passed = [False] * n
cnt = 0
nodes = [[] for _ in range(n)]
for _ in range(m):
    a, b = rm()
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

def dfs(x):
    passed[x] = True
    for next_node in nodes[x]:
        if passed[next_node] == False:
            dfs(next_node)

for i in range(n):
    if passed[i] == False:
        cnt += 1
        dfs(i)
print(cnt-1)