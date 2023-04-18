# 典型90-063
# PyPy only
# 普通にbit全探索すると2**h * 2**wで間に合わない
# hが極端に少ないことに着目しよう -> 2**h * wに帰着できないか？
# 行を全探索 -> 各列がすべて同要素になっているかをO(W*h_)で計算できる！
import sys
import itertools
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

h, w = rm()
pm = [rl() for _ in range(h)]
ans = 0
for r_ in range(h):
    for pl in itertools.combinations(pm, r=r_+1):
        counter = collections.Counter()
        for pcol_v in zip(*pl):
            if all(pv == pcol_v[0] for pv in pcol_v):
                counter[pcol_v[0]] += 1
            if len(counter):
                ans = max(counter.most_common(1)[0][1] * (r_+1), ans)
print(ans)
