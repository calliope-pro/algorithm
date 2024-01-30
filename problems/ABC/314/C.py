# ABC314-C
# 右に巡回シフトならdequeを使うと楽、オーダー的にも問題ない
import collections
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
s = rr()
cl = rl()
d = collections.defaultdict(lambda: collections.deque())
for cv, sv in zip(cl, s):
    d[cv].append(sv)
for k in d.keys():
    d[k].rotate(1)

ans = []
for cv in cl:
    ans.append(d[cv].popleft())
print("".join(ans))
