# PAST002-A
# 1Fを0とすることで数学的にできる
import sys

rs = lambda: sys.stdin.readline().split()

s, t = rs()
s = -int(s[1]) if s[0] == 'B' else int(s[0])-1
t = -int(t[1]) if t[0] == 'B' else int(t[0])-1
print(abs(t-s))
