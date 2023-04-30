# ABC019-B
# 典型的なRLE
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
ans = ''
for li in [[key, len(list(value))] for key, value in itertools.groupby(s)]:
    a, b = li
    ans += a + str(b)
print(ans)
