# ABC301-C
# atcoder, @以外の文字数は同じである
# atcoderの文字では、@で補填できるかどうかを調べる
import sys
import collections
from string import ascii_lowercase as al

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
t = rr()
cs = collections.Counter(s)
ct = collections.Counter(t)
r = 0
for c in al:
    if c not in {'a', 't', 'c', 'o', 'd', 'e', 'r'}:
        if ct[c] != cs[c]:
            print('No')
            exit()
    else:
        if ct[c] > cs[c]:
            if cs['@'] >= ct[c] - cs[c]:
                cs['@'] -= ct[c] - cs[c]
            else:
                print('No')
                exit()
        else:
            if ct['@'] >= cs[c] - ct[c]:
                ct['@'] -= cs[c] - ct[c]
            else:
                print('No')
                exit()
print('Yes' if cs['@'] == ct['@'] else 'No')
