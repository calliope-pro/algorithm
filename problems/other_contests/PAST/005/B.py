# PAST005-B
# 愚直にシミュレート
import sys

rr = lambda: sys.stdin.readline().rstrip()

rr()
s = rr()
t = ''
for c in s:
    t = t.replace(c, '') + c
print(t)
