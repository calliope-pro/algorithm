# PAST013-C
# 100C3 の組み合わせなので、普通に全探索するだけ
import sys
import itertools
from functools import reduce

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
s_ = set()
for co in itertools.combinations(al, r=3):
    s_.add(reduce(lambda x, y: x*y, co, 1))
print(len(s_))
