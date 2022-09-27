# ABC269-B
# 制約的に愚直にループ回す
import sys

rr = lambda: sys.stdin.readline().rstrip()

a, b, c, d = 1, 1, 1, 1
is_first = False
for i in range(1, 11):
    s = rr()
    if '#' in s:
        if not is_first:
            a = i
            c = s.index('#') + 1
            d = 10 - s[::-1].index('#')
            is_first = True
        b = i
print(a, b)
print(c, d)
