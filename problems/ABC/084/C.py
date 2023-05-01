# ABC084-C
# ある数以上の倍数の求め方だな。。
# 制約は小さいので、ループ回すだけでいい
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
csfl = [rl() for _ in range(n-1)]
ans = [0] * n
for idx, (c, s, f) in enumerate(csfl):
    for i in range(idx+1):
        ans[i] = max(s, -(-ans[i] // f) * f) + c
print(*ans, sep='\n')
