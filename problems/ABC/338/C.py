# ABC338-C
# numpyで楽したかったけど計算量的に無理そうだった
# Aがどれくらいできそうかを全探索して、Bの個数を計算していく
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n = ri()
ql = rl()
al = rl()
bl = rl()
ans = 0
for i_a in range(10**6+10):
    i_b = inf
    is_ok = True
    for qv, av, bv in zip(ql, al, bl):
        r = qv - av*i_a
        if r < 0:
            is_ok = False
            break
        if bv != 0:
            i_b = min(r//bv, i_b)
    if is_ok:
        ans = max(ans, i_a + i_b)
    if i_b == 0:
        break
print(ans)
