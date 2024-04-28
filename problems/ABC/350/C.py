# ABC350-C
# indexの入れ替えとリストの入れ替えを行う。単純だが嫌いな問題だ
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
cnt = 0
ans_l = []
d = {}
for i, av in enumerate(al, 1):
    d[av] = i
for k in range(1, n + 1):
    idx = d[k]
    if k != idx:
        cnt += 1
        ans_l.append((k, idx))
        al[k - 1], al[idx - 1] = k, al[k - 1]
        d[al[idx - 1]] = idx
print(cnt)
for ans in ans_l:
    print(*ans)
