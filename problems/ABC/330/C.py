# ABC330-C
# forの回数絞りつつ、浮動小数点の誤差を考慮すればガバガバ実装でもいける
import sys
import math

ri = lambda: int(sys.stdin.readline())
inf = float('inf')

d = ri()
ans = inf
for x in range(10**6 + 10):
    t = abs(x**2 - d)
    t = max(1, math.floor(math.sqrt(t)))
    for y in range(t-1, t+2):
        ans = min(ans, abs(x**2 + y**2 - d))
print(ans)
