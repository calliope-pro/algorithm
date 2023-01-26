# ABC277-C
# 1度探索したところは探索しなくていい + 次数が大きいことに注意すれば
# queue + BFSでもいい
import sys
import collections
import queue

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
nodes = collections.defaultdict(lambda: [])
passed = set([0])
for _ in range(n):
    a, b = rm()
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

q = queue.Queue()
q.put(0)
while not q.empty():
    node_now = q.get()
    for next_node in nodes[node_now]:
        if next_node not in passed:
            q.put(next_node)
            passed.add(next_node)  # ここで探索済みにaddしないと他からのパスでも追加される(次数が大きいため)
print(max(passed) + 1)
