# ABC331-C
# にぶたんと累積和を組み合わせて解く
import bisect
import itertools
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
sorted_al = sorted(al)
cum = tuple(itertools.accumulate([0]+sorted_al))
print(*(cum[-1] - cum[bisect.bisect_right(sorted_al, av)] for av in al))
