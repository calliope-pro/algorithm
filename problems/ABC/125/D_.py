# ABC125-D
# 面白い解き方
# dp使わずに規則性+貪欲
# 負の数は高々1つにできる -> 偶数個なのかどうか判定
# 負の数が存在してしまうなら、絶対値が一番少ないやつに押し付ける
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n = ri()
al = rl()
abs_sum = 0
mi_abs = inf
cnt_neg = 0
for av in al:
    if av < 0:
        cnt_neg ^= 1
    mi_abs = min(abs(av), mi_abs)
    abs_sum += abs(av)
if cnt_neg == 0:
    print(abs_sum)
else:
    print(abs_sum - 2*mi_abs)
