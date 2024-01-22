# ABC035-C
# いもす法だ、それぞれ何回ひっくり返るかを算出して、最後に色を出力する
import itertools
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, q = rm()
c = [0] * n
for _ in range(q):
    l, r = rm()
    c[l - 1] += 1
    if r < n:
        c[r] -= 1
print(*tuple(v & 1 for v in itertools.accumulate(c)), sep="")
