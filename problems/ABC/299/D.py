# ABC299-D
# 0_index -> 0, last_index -> 1なので、[0,1]区間が絶対存在する。
# この区間長を狭めればいい。->再帰とか2分探索で[0,1]区間を狭めていく
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
lb = 0
ub = n
while ub - lb > 1:
    mid = (ub + lb) // 2
    print(f'? {mid}', flush=True)
    s = ri()
    if s == 1:
        ub = mid
    else:
        lb = mid
print(f'! {lb}', flush=True)
