# ABC314-B
# うまくソートをしよう。閾値xの管理がだるい
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
v = []
for i in range(n):
    c = ri()
    al = set(rl())
    v.append((i, al, c))
x = ri()
a_ = sorted([v_ for v_ in v if x in v_[1]], key=lambda x: x[2])
if len(a_) == 0:
    print(0)
    exit()
ans = [a[0]+1 for a in a_ if a[2] == a_[0][2]]
print(len(ans))
print(*ans)
