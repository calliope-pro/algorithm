import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
t = rr()
s = itertools.groupby(s)
t = itertools.groupby(t)
for (sc, tc) in itertools.zip_longest(s, t):
    if sc is None or tc is None:
        print('No')
        exit()
    len_s = len(tuple(sc[1]))
    len_t = len(tuple(tc[1]))
    if sc[0] != tc[0]:
        print('No')
        exit()
    if len_s > len_t:
        print('No')
        exit()
    if (l:=len(tuple(sc[1]))) == 1 and len_t > 1:
        print('No')
        exit()
    print(l)
print('Yes')