# ABC311C
# dfs2回するだけ
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
passed = set()
i = 0
while i not in passed:
    passed.add(i)
    i = al[i] - 1

t = 0
ans = [i]
while True:
    t += 1
    if al[ans[-1]] - 1 == ans[0]:
        break
    ans.append(al[ans[-1]] - 1)
print(t)
print(*[v + 1 for v in ans])
