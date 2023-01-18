# ABC211-D
# BFS, ダイクストラの要領でやればいい
# 答え用のcnt, 長さのdistance, 頂点の探索状態のpassedをしっかりと条件分岐で管理
# queueへの待機状態を0, 探索済みを1にして実装した
import sys
import queue

rm = lambda: map(int, sys.stdin.readline().split())
inf = float('inf')
mod1 = 10**9 + 7

n, m = rm()
nodes = [[] for _ in range(n)]
for _ in range(m):
    a, b = rm()
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)
cnt = [0] * n
distance = [inf] * n
passed = [-1] * n
cnt[0] = 1
distance[0] = 0
q = queue.Queue()
q.put(0)
while q.qsize():
    node = q.get()
    passed[node] = 1
    for next_node in nodes[node]:
        if passed[next_node] == 1:
            continue
        if passed[next_node] == -1:
            q.put(next_node)
        passed[next_node] = 0
        if distance[next_node] > distance[node] + 1:
            distance[next_node] = distance[node] + 1
            cnt[next_node] = cnt[node] % mod1
        elif distance[next_node] == distance[node] + 1:
            cnt[next_node] += cnt[node]
            cnt[next_node] %= mod1
print(cnt[-1] % mod1)
