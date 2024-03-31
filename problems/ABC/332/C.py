# ABC332-C
# それぞれの区間について必要枚数を考えると良い
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
s = rr()
ans = 0
for c in s.split('0'):
    ans = max(max(c.count('1'), m)-m + c.count('2'), ans)
print(ans)
