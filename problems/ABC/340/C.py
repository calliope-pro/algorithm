# ABC340-C
# いやー脳死のlru_cacheによるメモ化再帰でいいな
import sys
from functools import lru_cache

ri = lambda: int(sys.stdin.readline())

n = ri()


@lru_cache(None)
def f(x: int):
    if x == 1:
        return 0
    return f((x + 1) // 2) + f(x // 2) + x


print(f(n))
