# ABC300-E
# さすがE問題初見では解けなかった。
# 1/5の遷移確率になることを漸化式で導けるようになりたい
# 漸化式からdpで求められる
# 1/5を掛ける = 5の逆元をかける
# あと、lru_cache、max_sizeデフォルトがNoneではなく128ってことに初めて気づいた
import sys
from functools import lru_cache

ri = lambda: int(sys.stdin.readline())
mod2 = 998244353

sys.setrecursionlimit(10000000)

N = ri()
inv = pow(5, -1, mod2)
@lru_cache(None)
def dp(n: int):
    if n > N:
        return 0
    if n == N:
        return 1
    return pow((dp(2*n) + dp(3*n) + dp(4*n) + dp(5*n) + dp(6*n)) * inv, 1, mod2)
print(dp(1))
