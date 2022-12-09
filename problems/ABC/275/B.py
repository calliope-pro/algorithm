# ABC275-B
# mod2の余りを事前に計算する下処理をした
import sys

mod2 = 998244353

a, b, c, d, e, f = map(lambda x: int(x)%mod2, sys.stdin.readline().split())
print((a*b*c - d*e*f) % mod2)
