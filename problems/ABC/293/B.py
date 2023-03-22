# ABC293-B
# O(N)で充分速いから脳死でループ
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
checked = [False] * n
for i in range(n):
    if not checked[i]:
        checked[al[i] - 1] = True
ans = []
for i, is_checked in enumerate(checked):
    if not is_checked:
        ans.append(i+1)
print(len(ans))
print(*ans)
