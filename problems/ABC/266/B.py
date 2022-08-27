# ABC266-B
# いくら引けば倍数になるか。
# modを取ればいい
import sys

ri = lambda: int(sys.stdin.readline())
mod2 = 998244353

n = ri()
print(n % mod2)
