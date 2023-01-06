# 典型90-052
# それぞれの列の組み合わせの積の和は、それぞれの行の和の積になることに気付く必要あり
# 因数分解で証明可能
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))
mod1 = 10**9 + 7

n = ri()
ans = 1
for _ in range(n):
    ans *= sum(rl())
print(ans % mod1)
