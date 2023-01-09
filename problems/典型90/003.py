# 典型90-003
# 双方向パスであるが、あまりここでは関係ないと気付くこと
# 任意の点から一番深い点Pから再度一番深い点QのP-Q間が最長である -> dfsを2度行う
# 探索済みはリストで0,1管理するか、関数の引数で持たせるか、等で工夫
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10000000)

n = ri()
ab = [set() for _ in range(n)]
for _ in range(n-1):
    a, b = rm()
    ab[a-1].add(b-1)
    ab[b-1].add(a-1)

def dfs(k=0, b=None):
    cnt = 0
    p = k
    for i in ab[k]:
        if i == b:
            continue
        res = dfs(i, k)
        if res[0] + 1 > cnt:
            cnt = res[0] + 1
            p = res[1]
    return cnt, p

f = dfs()[1]
print(dfs(f)[0] + 1)
