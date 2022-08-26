# hhkb2020-B
# 回転させてあとは愚直に走査
import sys
from typing import List, Sequence

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

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
sl = [rr() for _ in range(h)]
ans = 0
for s in sl:
    for i in range(w-1):
        if s[i] == s[i+1] == '.':
            ans += 1

for s in rotate90(sl):
    for i in range(h-1):
        if s[i] == s[i+1] == '.':
            ans += 1

print(ans)
