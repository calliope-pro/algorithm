# ABC257-C
# 人数は10**5オーダーなので、各人の体重をべースにスコアを二分探索で算出した
# (全員が子供といったコーナーケースに対処するために最大と最小体重の幅を伸ばした)
# 想定解は最小体重の人から基準を増やしていくもの
import bisect
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
s = rr()
wl = rl()
children = []
adults = []
for s_, wv in zip(s, wl):
    if s_ == '0':
        children.append(wv)
    else:
        adults.append(wv)
children = sorted(children)
adults = sorted(adults)
len_adults = len(adults)
ans = 0
wl += [max(wl)+1, min(wl)-1]
for wv in wl:
    score = bisect.bisect_left(children, wv) + len_adults - bisect.bisect_left(adults, wv)
    ans = max(score, ans)
print(ans)
