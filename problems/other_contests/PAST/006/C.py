# PAST006-C
# set型の有難さ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
a = [set(rl()[1:]) for _ in range(n)]
p, q = rm()
b_set = set(rl())
cnt = 0
for a_set in a:
    cnt += len(a_set & b_set) >= q
print(cnt)
