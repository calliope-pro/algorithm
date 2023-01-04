# PAST009-C
# 愚直にシミュレート、条件分岐をしっかりと
import sys
from string import ascii_uppercase

rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
au = ascii_uppercase

n = ri()
ans = [0]*6
for i in range(1, n+1):
    problem, judge = rs()
    if judge == 'AC' and ans[au.index(problem)] == 0:
        ans[au.index(problem)] = i
print(*ans, sep='\n')
