# 典型90-076
# 1/10と9/10の大きさのどちらかは連続列として必ずでることを利用した
# 列の長さを2倍にしてシミュレートするのが想定解らしい
import sys
import itertools

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = [0] + rl()
cum = list(itertools.accumulate(al))
set_ = set(cum)
if cum[-1] % 10 != 0:
    print('No')
    exit()
p = cum[-1] // 10
for pv in cum:
    if (pv + p) in set_ or (pv + p*9) in set_:
        print('Yes')
        exit()
print('No')
