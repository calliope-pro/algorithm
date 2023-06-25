# ABC233-D
# これ単純なのに苦手だな。
# ナイーブな解法から短縮を図る
import sys
import itertools
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
al = rl()
ans = 0
cum = list(itertools.accumulate([0]+al))
counter = collections.Counter(cum)

# これがナイーブ
# for i, v in enumerate(cum):
#     for v_ in cum[i+1:]:
#         if v - v_ == k:
#             ans += 1

for i, v in enumerate(cum):
    counter[v] -= 1
    ans += counter[v+k]
print(ans)
