# 典型90-046
# 46で割った余りで個数をそれぞれ管理すると全探索で計算量を減らせる
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()
b = rl()
c = rl()
a_cnt = [0]*46
b_cnt = [0]*46
c_cnt = [0]*46
for av in a:
    a_cnt[av%46] += 1
for bv in b:
    b_cnt[bv%46] += 1
for cv in c:
    c_cnt[cv%46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += a_cnt[i]*b_cnt[j]*c_cnt[k]
print(ans)
