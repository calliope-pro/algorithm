# ABC333-B
# 正五角形の線分の長さは2つしかない->組み分けて考える
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = ''.join(sorted(rr()))
t = ''.join(sorted(rr()))
if s in {'AB', 'BC', 'CD', 'DE', 'AE'} and t in {'AB', 'BC', 'CD', 'DE', 'AE'}:
    print('Yes')
elif s not in {'AB', 'BC', 'CD', 'DE', 'AE'} and t not in {'AB', 'BC', 'CD', 'DE', 'AE'}:
    print('Yes')
else:
    print('No')
