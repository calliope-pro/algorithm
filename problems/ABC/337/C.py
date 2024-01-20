# ABC337-C
# 先頭を見つけて芋づる方式で探索する
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
di = {ai: i for i, ai in enumerate(al)}
ans = [di[-1] + 1]
for _ in range(n - 1):
    prev = ans[-1]
    ans.append(di[prev] + 1)
print(*ans)
