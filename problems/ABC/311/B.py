# ABC311-B
# oxをメモして、最大の連続するoの数を出力するだけ
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, d = rm()
days = [0] * d
for _ in range(n):
    s = rr()
    for day, c in enumerate(s):
        days[day] = max(days[day], int(c=='x'))
ans = 0
for chunk in itertools.groupby(days):
    if chunk[0] == 0:
        ans = max(ans, len(list(chunk[1])))
print(ans)
