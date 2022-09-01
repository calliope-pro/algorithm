# ABC258-C
# インデックスの管理が出来ればあとは単にスライス
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, q = rm()
s = rr()
cut = 0
for _ in range(q):
    idx, x = rm()
    if idx == 1:
        cut = (cut + x) % n
    else:
        print(s[(-cut+x-1)%n])
