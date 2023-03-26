# ABC295-A
# 全て包含されているか、`or`をモノイドのFalseで再代入
import sys

rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())

n = ri()
wl = rs()
f = False
for s in ['and', 'not', 'that', 'the', 'you']:
    f = (s in wl) or f
if f:
    print('Yes')
else:
    print('No')
