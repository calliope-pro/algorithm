# ABC307-B
# itertoolsで順列とってくるの楽すぎ
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
sl = [rr() for _ in range(n)]
for x, y in itertools.permutations(sl, 2):
    s = x + y
    if s == s[::-1]:
        print('Yes')
        exit()
print('No')
