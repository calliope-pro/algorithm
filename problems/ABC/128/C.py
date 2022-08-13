# ABC128-C
# bit全探索
# setを上手く入れて楽に実装
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
switches = [set(rl()[1:]) for _ in range(m)]
p = rl()
cnt = 0
for i in range(n+1):
    for co in itertools.combinations(range(1, n+1), i):
        for switch, pv in zip(switches, p):
            if len(switch & set(co)) % 2 != pv:
                break
        else:
            cnt += 1
print(cnt)
