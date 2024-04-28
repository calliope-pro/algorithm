# ABC350-A
# intに変換して条件分岐するだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
n = int(s[-3:])
if 1 <= n <= 315 or 317 <= n <= 349:
    print('Yes')
else:
    print('No')
