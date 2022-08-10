# ABC238-C
# 場合分けする。数学的計算を実装
import sys

ri = lambda: int(sys.stdin.readline())
mod2 = 998244353

n = ri()
l = len(str(n))
ans = 0
for i in range(1, l):
    bef = 10**(i-1) - 1
    aft = 10**i - 1
    ans += (1+aft-bef) * (aft - bef) // 2
    ans %= mod2
bef = 10**(l-1) - 1
aft = n
ans += (1+aft-bef) * (aft - bef) // 2
ans %= mod2
print(ans)
