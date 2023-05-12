# PAST012-C
# インデックスと合計がリンクしているよ
# 確率は場合の数だと考えて、最後に割り算することで誤差を減らした
import sys

rl = lambda: list(map(int, sys.stdin.readline().split()))

p1 = rl()
p2 = rl()
p3 = rl()
ans = [0] * 18
for i in range(6):
    for j in range(6):
        for k in range(6):
            ans[i+j+k+3-1] += p1[i]*p2[j]*p3[k]
for ans_v in ans:
    print(ans_v / (100**3))
