# ABC299-A
# 久しぶりにリアル参加したのにUnratedかー
# 2個しかないので、それぞれのインデックスを取得すればいい
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
l = s.index('|')
r = s.index('|', l+1)
if s[l:r].count('*') != 0:
    print('in')
else:
    print('out')
