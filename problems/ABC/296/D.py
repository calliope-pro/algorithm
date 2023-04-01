# ABC296-D
# 10**12 -> O(N**0.5)とかになるかを検討しよう
# a*bはM以上になればいい。Mは10**12 -> aがM**0.5以下でbがN以下になるかを調べればいい
# 実装では、ルートをとるときの誤差を加味して実装すべし
import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())
inf = float('inf')

n, m = rm()
ans = inf
for a in range(1, math.floor(m**0.5)+100):
    b = math.ceil(m/a)
    if a <= n and b <= n:
        ans = min(ans, a*b)
if ans is not inf:
    print(ans)
else:
    print(-1)
