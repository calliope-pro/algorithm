# ABC257-C
# 想定解は最小体重の人から基準を増やしていくもの
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
s = rr()
wl = rl()
sw = [(wv, s_) for s_, wv in zip(s, wl)] + [(10**10, '')]  # 最後の人対策で最大制約越えを与える
sw.sort()
score = s.count('1')  # 最小体重 -> 大人の人数だけ正解
ans = score
for i in range(n):
    if sw[i][1] == '1':
        score -= 1
    else:
        score += 1

    if sw[i][0] != sw[i+1][0]:  # 次の人と違う体重のときだけスコアが更新
        ans = max(score, ans)
print(ans)

