# ABC270-C
# dfsを使う
# 初見ではノードはpassedに通った順を記録することで対応した
# 想定解 -> stackを更に組み合わせて使うことで、ノードを記録している
import sys

rm = lambda: map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10000000)

n, x, y = rm()
x -= 1
y -= 1
paths = [[] for _ in range(n)]
passed = [0] * n

for _ in range(n-1):
    u, v = rm()
    paths[u-1].append(v-1)
    paths[v-1].append(u-1)

# 通った順リスト
def dfs(k, p=1):
    passed[k] = p
    for node in paths[k]:
        if node == y:
            ans = []
            for i, v in enumerate(passed, 1):
                if v > 0:
                    ans.append((v, i))
            print(*([ans_t[1] for ans_t in sorted(ans)] + [y+1]))
            return
        if passed[node] == 0:
            dfs(node, p+1)
            passed[node] = 0
dfs(x)

# stackによる実装
import queue
stack = queue.LifoQueue()
stack.put(x+1)
def dfs(k):
    passed[k] = 1
    for node in paths[k]:
        stack.put(node+1)
        if node == y:
            print(*stack.queue)
            return True
        if passed[node] == 0:
            if dfs(node):
                return
            passed[node] = 0
        stack.get()
dfs(x)
