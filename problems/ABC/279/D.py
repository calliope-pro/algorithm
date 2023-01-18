# ABC279-D
# 制約が大きい -> 二分探索などのlogを考える
# 関数の下への凸性を利用し、あるmidの周辺を調査することで勾配が掴める
# 想定解は三分探索
import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
def time(t):
    if t < 0:
        return a
    return a/math.sqrt(t+1) + b*t
lb = 0
ub = 10**18+10
while ub - lb > 1:
    mid = (ub + lb) // 2
    if mid == 0:
        print(min(time(mid), time(mid+1)))
        exit()
    if time(mid-1) <= time(mid) <= time(mid+1):
        ub = mid
    elif time(mid-1) >= time(mid) and time(mid) <= time(mid+1):
        print(time(mid))
        exit()
    else:
        lb = mid
print(min(time(lb-1), time(lb), time(lb+1)))
