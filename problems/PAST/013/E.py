# PAST013-E
# 累積和で考える。常に正`(`が`)`より多い + 最終的に`(`と`)`が同じ数になるか
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
tmp = 0
for c in s:
    if c == '(':
        tmp += 1
    else:
        tmp -= 1
    if tmp < 0:
        print('No')
        exit()
if tmp == 0:
    print('Yes')
else:
    print('No')
