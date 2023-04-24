# ABC298-B
# bit演算使っておしゃんな解き方できた
# aにあるものはbに必ず含まれる集合と同じ
import sys

if 'PyPy' not in sys.version:
    import numpy as np

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))


n = ri()
am = [rl() for _ in range(n)]
bm = [rl() for _ in range(n)]
am = np.array(am)
for _ in range(4):
    cm = am & bm
    if (am != cm).sum() == 0:
        print('Yes')
        exit()
    am = np.rot90(am)
print('No')


