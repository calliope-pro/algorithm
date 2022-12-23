# ABC282-B
# 組み合わせはitertools.combinationsを使い
# 判定をanyを使って短くした
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
li = [rr() for _ in range(n)]
cnt = 0
for (s1, s2) in itertools.combinations(li, 2):
    cnt += not any(c1 == c2 == 'x' for c1, c2 in zip(s1, s2))
print(cnt)
