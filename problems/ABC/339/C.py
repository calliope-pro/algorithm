# ABC339-C
# まず最低何人いないといけないかを求める
# そのあとに最終時点までの増減を足し合わせる
import itertools
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = [0]+rl()
cum = tuple(itertools.accumulate(al))
p0 = abs(min(cum))
print(p0+cum[-1])
