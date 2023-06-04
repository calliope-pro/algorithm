# ABC218-C
# 結構苦しんだ。。
# '.'によるpaddingが無いと考えた際の'#'位置を照らせるようにした。
import sys
import itertools
from typing import List, Sequence

rsl = lambda: list(sys.stdin.readline().rstrip())
ri = lambda: int(sys.stdin.readline())
inf = float('inf')

def rotate90(m: Sequence[Sequence]) -> List[tuple]:
    '''
    二次元の配列やシーケンスを右に90度回転

    Parameters
    ----------
    m : Sequence[Sequence]
        回転させたい二次元配列およびそれに近しいシーケンス

    Returns
    -------
    List[tuple]
        回転後の行列
    '''
    return list(zip(*m[::-1]))

n = ri()
s = [rsl() for _ in range(n)]
t = [rsl() for _ in range(n)]
tx = inf
ty = inf
for i, tr in enumerate(t):
    if '#' in tr:
        tx = min(i, tx)
        ty = min(tr.index('#'), ty)

for _ in range(4):
    sx = inf
    sy = inf
    dx = 0
    for i, sr in enumerate(s):
        if '#' in sr:
            sx = min(i, sx)
            sy = min(sr.index('#'), sy)
    for tr, sr in itertools.zip_longest(t[tx:], s[sx:], fillvalue=[]):
        tr = tr[ty:]
        sr = sr[sy:]
        l = min(len(tr), len(sr))
        tr_ = ''.join(tr[:l])
        sr_ = ''.join(sr[:l])
        if tr_ != sr_ or '#' in tr[l:] or '#' in sr[l:]:
            break
    else:
        print('Yes')
        exit()
    s = rotate90(s)
print('No')
