# ABC294-B
# ループと文字変換するだけ
import sys
from string import ascii_uppercase

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
au = ascii_uppercase

h, w = rm()
for _ in range(h):
    al = rl()
    for av in al:
        if av == 0:
            print('.', end="")
        else:
            print(au[av-1], end="")
    print()
