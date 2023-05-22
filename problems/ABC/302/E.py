# ABC302-E
# 425点だから簡単
# エッジ数の変動があればノード数を監視すればいい
# とてもナイーブである
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, q = rm()
nodes = [set() for _ in range(n)]
ans = n
for _ in range(q):
    query = rl()
    if query[0] == 1:
        u, v = query[1], query[2]
        if len(nodes[u-1]) == 0:
            ans -= 1
        if len(nodes[v-1]) == 0:
            ans -= 1
        nodes[u-1].add(v-1)
        nodes[v-1].add(u-1)
    else:
        v = query[1]
        for next_node in nodes[v-1]:
            if v-1 in nodes[next_node]:
                nodes[next_node].remove(v-1)
                if len(nodes[next_node]) == 0:
                    ans += 1
        if len(nodes[v-1]) != 0:
            ans += 1
            nodes[v-1] = set()
    print(ans)
