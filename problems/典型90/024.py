# 典型90-024
# 条件をしっかりと見極める
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
al = rl()
bl = rl()
steps_min = sum(abs(av-bv) for av, bv in zip(al, bl))
if steps_min <= k and (k-steps_min) % 2 == 0:
    print('Yes')
else:
    print('No')
