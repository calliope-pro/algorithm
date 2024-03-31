# ABC333-C
# Nが最大の時の答えが出ているので、高々13C3の組み合わせを全探索して答えを求める
import itertools
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
l = []
for co in itertools.combinations_with_replacement(["1" * i for i in range(1, 13)], 3):
    l.append(sum(map(int, co)))
l.sort()
print(l[n-1])
