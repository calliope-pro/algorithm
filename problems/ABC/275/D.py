# ABC275-D
# キャッシュでごり押し
import sys
from functools import lru_cache

ri = lambda: int(sys.stdin.readline())

n = ri()
@lru_cache
def f(x):
    if x == 0:
        return 1
    return f(x//2) + f(x//3)
print(f(n))
