# ABC223-D
# 初のトポロジカルソート。。
# 面白いけどソート感無いな〜
# 入次数が0が先頭、その要素が前になるのが確定したら、その他のようでまた入次数を計算して0のものを先頭にする。これの繰り返し
import sys
import heapq

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
nodes = [set() for _ in range(n)]
counter = [0] * n # 入次数
for _ in range(m):
    a, b = rm()
    a -= 1
    b -= 1
    if b not in nodes[a]:
        nodes[a].add(b)  # A->B
        counter[b] += 1

h = []
for node, cnt in enumerate(counter):
    if cnt == 0:
        h.append(node)

heapq.heapify(h)
ans = []
while len(h):
    node = heapq.heappop(h)
    ans.append(node+1)

    for next_node in nodes[node]:
        counter[next_node] -= 1  # 入次数を1減らす
        if counter[next_node] == 0:
            heapq.heappush(h, next_node)

if len(ans) == n:
    print(*ans)
else:
    print(-1)


