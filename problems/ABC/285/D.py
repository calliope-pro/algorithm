# ABC285-D
# 次数が2以下、閉路無しだと良い -> 木であるかどうか
import sys

rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())

sys.setrecursionlimit(10000000)

n = ri()
dict_ = {}
nodes = [[] for _ in range(2*n)]
passed = [0] * 2*n
for i in range(n):
    s, t = rs()
    s_ = dict_.get(s, i*2)
    dict_[s] = s_
    t_ = dict_.get(t, i*2 + 1)
    dict_[t] = t_
    nodes[s_].append(t_)
    nodes[t_].append(s_)
for node in nodes:
    if len(node) > 2:
        print('No')
        exit()

def dfs(k, prev=None):
    passed[k] = True
    for node in nodes[k]:
        if node == prev:
            continue
        if passed[node] == True:
            print('No')
            exit()
        dfs(node, k)

for i in range(2*n):
    if passed[i] == 0:
        dfs(i)
print('Yes')
