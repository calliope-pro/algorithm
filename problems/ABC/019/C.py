# ABC019-C
# 要素を2で割り切れるまでやった値を計算して高速化のためにメモ化
import sys
from functools import lru_cache

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
set_ = set()
@lru_cache(None)
def f(x: int):
    if x&1:
        return x
    return f(x>>1)
for av in al:
    set_.add(f(av))
print(len(set_))
