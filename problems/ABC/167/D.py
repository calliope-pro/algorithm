# ABC167-D
# 閉路検出すれば、あとは制約的にループ出来る
# 通った順をpassedに保存しておくと計算できるので楽
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
al = rl()
passed = [-1] * n
passed[0] = 0
node = 0
while True:
    next_node = al[node] -1 
    if passed[next_node] != -1:
        loop_cnt = passed[node] - passed[next_node] + 1
        k -= passed[node]
        k %= loop_cnt
        for _ in range(k):
            next_node = al[node] - 1
            node = next_node
        print(node+1)
        break
    if passed[node] == k-1:
        print(next_node+1)
        break
    passed[next_node] = passed[node] + 1
    node = next_node
