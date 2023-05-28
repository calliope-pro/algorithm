# ABC125-C
# 双方向貪欲法での実装、これ色々使えそう
# Nなので速い
import sys
import math
import itertools

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()

lgcd = tuple(itertools.accumulate(al, math.gcd))
rgcd = tuple(reversed(tuple(itertools.accumulate(al[::-1], math.gcd))))
ans = max(lgcd[n-2], rgcd[1])
for i in range(1, n-1):
    ans = max(math.gcd(lgcd[i-1], rgcd[i+1]), ans)
print(ans)
