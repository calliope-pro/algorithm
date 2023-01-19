# ABC229-D
# 置換する -> 置換の個数の上限がある -> 累積和を使い、差分で置換の個数を求める
# 累積和っぽくなくても使えるようになると楽
import bisect
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

s = rr()
k = ri()
cum = [0]
for c  in s:
    if c == '.':
        cum.append(cum[-1] + 1)
    else:
        cum.append(cum[-1])
ans = 0
for idx, cum_v in enumerate(cum):
    ans = max(bisect.bisect_right(cum, cum_v+k) - 1 - idx, ans)
print(ans)
