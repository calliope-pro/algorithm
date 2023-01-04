# PAST004-A
# np.argsort使うと楽
# numpy使わないならタプル使って複数キーでソート
import sys
import numpy as np

rl = lambda: list(map(int, sys.stdin.readline().split()))

print('ABC'[np.argsort(rl())[1]])
