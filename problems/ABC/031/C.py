# ABC031-C
# 眠すぎ。頭回らん
# 制約小さいので、単純に全探索でいい
# とりうる数列の候補を全列挙
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n = ri()
al = rl()
ans = -1000
for i in range(n):
    tmp = -inf
    ans_ = -inf
    for j in range(n):
        if i == j:
            continue
        aoki = sum(al[min(j, i)+1:max(i, j)+1:2])
        taka = sum(al[min(j, i):max(i, j)+1:2])
        if aoki > tmp:
            tmp = aoki
            ans_ = taka
    ans = max(ans, ans_)
print(ans)
