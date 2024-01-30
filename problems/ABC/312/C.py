# ABC312-C
# にぶたんでNlogN
# すべての要素とその要素+1について妥当であるかを判定する、ソートしてるのでbreakで抜けるとよい
import bisect
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n, m = rm()
al = rl()
al.sort()
bl = rl()
bl.sort()
ans = inf
for v in sorted(al+bl):
    a_cnt = bisect.bisect_right(al, v) + 1
    b_cnt = m - bisect.bisect_left(bl, v) + 1
    if a_cnt >= b_cnt:
        ans = min(ans, v)
        break
    v += 1
    a_cnt = bisect.bisect_right(al, v) + 1
    b_cnt = m - bisect.bisect_left(bl, v) + 1
    if a_cnt >= b_cnt:
        ans = min(ans, v)
        break
print(ans)
