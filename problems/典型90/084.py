# 典型90-084
# oのみとxのみの区間の組み合わせを考える(余事象)
# あとはRLEすると良い
import sys
import itertools
from scipy.special import comb

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
s_ = itertools.groupby(s)
ans = comb(n+1, 2, exact=True)
for c, l in s_:
    ans -= comb(len(tuple(l))+1, 2, exact=True)
print(ans)
