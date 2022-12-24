# ABC272-C
# 条件分岐するだけ
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()
s_e = []
s_o = []
for a_ in a:
    if a_&1:
        s_o.append(a_)
    else:
        s_e.append(a_)
ans = 0
if len(s_e) > 1:
    ans = max(ans, sum(sorted(s_e)[-2:]))
if len(s_o) > 1:
    ans = max(ans, sum(sorted(s_o)[-2:]))
if ans == 0:
    print(-1)
    exit()
print(ans)
