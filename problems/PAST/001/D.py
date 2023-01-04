# PAST001-D
# set型使って計算量を減らす
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
s = set(range(1, n+1))
ans = None
for _ in range(n):
    a = ri()
    if a in s:
        s.discard(a)
    else:
        ans = a

if ans is None:
    print('Correct')
else:
    print(ans, s.pop())
