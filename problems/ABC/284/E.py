# ABC284-E
# DFSと探索済みリストの融合
# TLE対策として、10**6より大きい答えは10**6とされているの嬉しい
import sys

rm = lambda: map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10000000)

n, m = rm()
uv = [[] for _ in range(n)]
passed = [0 for _ in range(n)]
for _ in range(m):
    u, v = rm()
    uv[u-1].append(v-1)
    uv[v-1].append(u-1)

def dfs(k=0):
    passed[k] = 1  # dfsに入ったら探索済みにする
    cnt = 1
    for node in uv[k]:
        if passed[node] == 0:
            cnt += dfs(node)  # nodeからのdfs
            passed[node] = 0  # 次のnodeからのdfsなので、探索リストは0にしておく
        if cnt > 10**6:
            return 10**6
    return cnt

print(dfs())
