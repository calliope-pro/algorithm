# PAST004-E
# 制約が小さいので、順列使って全探索していい
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
for co in itertools.permutations(s):
    tmp = ''.join(co)
    if tmp != s and tmp[::-1] != s:
        print(tmp)
        exit()
print('None')
