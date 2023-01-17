# ABC285-C
# n進数の性質を利用するだけや
import sys
from string import ascii_uppercase

rr = lambda: sys.stdin.readline().rstrip()
au = ascii_uppercase

s = rr()
ans = 0
for i, c in enumerate(s[::-1]):
    n = au.index(c) + 1
    ans += n * (26**i)
print(ans)
