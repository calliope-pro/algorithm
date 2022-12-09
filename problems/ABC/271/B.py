# ABC271-B
# 2次配列を上手く管理するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, q = rm()
lines = []
for _ in range(n):
    l, *line = rm()
    lines.append(line)
for _ in range(q):
    s, t = rm()
    print(lines[s-1][t-1])
