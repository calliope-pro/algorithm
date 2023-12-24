# ABC321-A
# 文字で比較でOK
import sys

rr = lambda: sys.stdin.readline().rstrip()

n = rr()
if len(n) == 1:
    print('Yes')
    exit()
for (a, b) in zip(n, n[1:]):
    if a <= b:
        print('No')
        exit()
print('Yes')
