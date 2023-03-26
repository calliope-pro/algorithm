# ABC295-C
# collections.Counter使って個数を数え上げると楽。
# mapも使うと実質ワンライナー
import sys
import collections

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
print(sum(map(lambda x:x//2, collections.Counter(al).values())))


