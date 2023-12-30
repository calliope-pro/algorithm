# ABC317-B
# 一意に定まるなら、両端であるmin, maxのrangeにおさまるため、setで差分を取る
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
min_ = min(al)
max_ = max(al)
print(*(set(range(min_, max_ + 1)) - set(al)))
