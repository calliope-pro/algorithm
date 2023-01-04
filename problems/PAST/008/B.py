# PAST008-B
# set型
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
a = set(rm())
b = set(rm())
for v in sorted(a&b):
    print(v, end=' ')
