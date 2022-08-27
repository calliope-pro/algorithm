# PAST001-C
# ソートさせて後ろからピック
import sys

rl = lambda: list(map(int, sys.stdin.readline().split()))

li = rl()
li.sort()
print(li[-3])
