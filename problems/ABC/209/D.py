# ABC209-D
# まず制約から、連結・閉路無しの木であることを理解
# 木なのでBFSで、ある地点から奇数目なのか偶数目なのか事前に計算しておく
# 最後は計算した値同士から偶奇を判定
import sys
import queue

rm = lambda: map(int, sys.stdin.readline().split())

n, query = rm()
nodes = [[] for _ in range(n)]
nodeFlags = [-1] * n
nodeFlags[0] = 0
for _ in range(n-1):
    a, b = rm()
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

q = queue.Queue()
q.put(0)
while q.qsize():
    k = q.get()
    nodeFlag = nodeFlags[k]
    for node in nodes[k]:
        if nodeFlags[node] == -1:
            nodeFlags[node] = 1 - nodeFlag
            q.put(node)

for _ in range(query):
    c, d = rm()
    print(['Town', 'Road'][nodeFlags[c-1]^nodeFlags[d-1]])
