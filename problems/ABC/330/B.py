# ABC330-B
# 条件分岐が大事
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, l, r = rm()
al = rl()
ans = []
for a in al:
    if a <= l:
        ans.append(l)
    elif a >= r:
        ans.append(r)
    else:
        ans.append(a)
print(' '.join(map(str, ans)))
