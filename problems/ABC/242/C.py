# ABC242-C
# 人力DP
import sys

ri = lambda: int(sys.stdin.readline())
mod2 = 998244353

n = ri()
c_19 = 1
c_28 = 1
c_37 = 1
c_46 = 1
c_5 = 1
for _ in range(n-1):
    c_19, c_28, c_37, c_46, c_5 = c_19+c_28, c_19+c_28+c_37, c_28+c_37+c_46, c_37+c_46+c_5, c_46*2+c_5
    c_19 %= mod2
    c_28 %= mod2
    c_37 %= mod2
    c_46 %= mod2
    c_5 %= mod2
print(((c_19 + c_28 + c_37 + c_46)*2 + c_5) % mod2)
